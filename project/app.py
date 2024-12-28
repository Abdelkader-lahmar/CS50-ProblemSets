#Import libraries
import re
from flask import Flask, render_template, session, request, redirect , url_for
from flask_session import Session
from func import apology, decrypt, encrypt, login_required, fixdomain
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash
import secrets
#import for mail
from flask_mail import Mail, Message

app = Flask(__name__)

#Configer session(cookies)
app.secret_key = '5dcb00ba6b52ca0baddcad769c52e5e1806c0415546e56f532c18aec41789fe8' #This should be secret don't tell anyone
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configer the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Import the models
from model import users, passes, tokens
with app.app_context():
    db.create_all()

#fillter for jinja
app.jinja_env.filters["fixdomain"] = fixdomain

#Configer the mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'noreplay.cspass@gmail.com'
app.config['MAIL_PASSWORD'] = 'zqkr zaxb suhp yjws'
app.config['MAIL_DEFAULT_SENDER'] = 'noreplay.cspass@gmail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
    

@app.route('/')
@login_required
def vault():
    #querry the database for the passwords
    passwords = passes.query.filter_by(user_id=session["user_id"]).all()
    #render the vault page
    return render_template("vault.html", passwords=passwords, show_footer=True)


@app.route('/card', methods=["GET"])
@login_required
def card():
    if request.args.get("type") == "add":
        #render the add card page
        return render_template("card.html", show_footer=True, type="add")
    elif request.args.get("type") == "edit":
        #get the id of the password
        id = request.args.get("id")
        #verify that the password belong to the user
        password = passes.query.filter_by(id=id, user_id=session["user_id"]).first()
        if password:
            #decrypt the password
            password.password = decrypt(password.password, session["user_password"].encode(), session["user_salt"])
            #render the edit card page
            return render_template("card.html", show_footer=True, type="edit", password=password)
        else:
            return apology("Password not found")
    return apology("Wrong request")


@app.route('/addcard', methods=["POST"])
@login_required
def add_card():
    #if the user submit the form
    if request.method == "POST":
        domain = request.form.get("domain")
        email = request.form.get("email")
        password = request.form.get("password")
        #Regular expression for validate email and password idea taken from chatgpt
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        PASSWORD_REGEX = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[?!@#$%^&*]).{8,}")
        if domain and email and password and EMAIL_REGEX.match(email) and PASSWORD_REGEX.match(password):
            #encrypt the password
            password = encrypt(password, session["user_password"].encode(), session["user_salt"])
            try:
                #add the password to the database
                new_pass = passes(domain=domain, email=email, password=password, user_id=session["user_id"])
                db.session.add(new_pass)
                db.session.commit()
            except IntegrityError:
                return apology("Password already Exist")
            else:
                return redirect("/")
        else:
            return apology("Wrong information")
        
        
@app.route('/editcard', methods=["POST"])
@login_required
def editcard():
    id = request.form.get("id")
    password = passes.query.filter_by(id=id, user_id=session["user_id"]).first()
    if password:
        new_domain = request.form.get("domain")
        new_email = request.form.get("email")
        new_password = request.form.get("password")
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        PASSWORD_REGEX = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[?!@#$%^&*]).{8,}")
        if new_domain and new_email and new_password and EMAIL_REGEX.match(new_email) and PASSWORD_REGEX.match(new_password):
            password.domain = new_domain
            password.email = new_email
            password.password = encrypt(new_password, session["user_password"].encode(), session["user_salt"])
            db.session.commit()
            return redirect("/")
        else:
            return apology("Wrong information")
    else:
        return apology("Password not found")


@app.route('/deletcard', methods=["GET"])
@login_required
def deletcard():
    id = request.args.get("id")
    password = passes.query.filter_by(id=id, user_id=session["user_id"]).first()
    if password:
        db.session.delete(password)
        db.session.commit()
        return redirect("/")
    else:
        return apology("Password not found")


@app.route('/account', methods=["GET", "POST"])
@login_required
def account():
    #if the user submit the form
    if request.method == "POST":
        session.clear()
        return redirect("/login")
    user = users.query.filter_by(id=session["user_id"]).first()
    #render the account page
    return render_template("account.html", show_footer=True, user=user)


@app.route('/changeinfo', methods=["POST"])
@login_required
def changeinfo():
    #get the name and email from the form
    name = request.form.get("name")
    email = request.form.get("email")
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if name and email and email_regex.match(email):
        #update the user information
        user = users.query.filter_by(id=session["user_id"]).first()
        user.user_name = name
        user.user_email = email
        db.session.commit()
        return redirect("/account")
    else:
        return apology("Wrong information")


@app.route('/changepass', methods=["POST"])
@login_required
def changepass():
    old_pass = request.form.get("old_password")
    new_pass = request.form.get("password")
    confirm = request.form.get("confirm")
    PASSWORD_REGEX = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[?!@#$%^&*]).{8,}")
    if old_pass and new_pass and confirm and new_pass == confirm and PASSWORD_REGEX.match(new_pass):
        user = users.query.filter_by(id=session["user_id"]).first()
        #check if the old password is correct
        if check_password_hash(user.master_pass, old_pass):
            #decrypt the passes database
            passwords = passes.query.filter_by(user_id=session["user_id"]).all()
            for password in passwords:
                password.password = decrypt(password.password, session["user_password"].encode(), session["user_salt"])
            #update the password
            user.master_pass = generate_password_hash(new_pass)
            session["user_password"] = new_pass
            #re-encrypt the passwords
            for password in passwords:
                password.password = encrypt(password.password, session["user_password"].encode(), session["user_salt"])
            db.session.commit()
            return redirect("/account")
        else:
            return apology("Wrong password")
    else:
        return apology("Wrong information")


@app.route("/login", methods=["GET", "POST"])
def login():
    #clear the session
    session.clear()
    #if the user submit the form
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            #check if the user exist
            user = users.query.filter_by(user_email=email).first()
            if user:
                #check if the password is correct
                if check_password_hash(user.master_pass, password):
                    session["user_id"] = user.id
                    session["user_password"] = password
                    session["user_salt"] = user.user_salt
                    return redirect("/")
                else:
                    return apology("Wrong password")
            else:
               return apology("User not found")
        else:
            return apology("Wrong email/password")
    
    #render the login page
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    #clear the session
    session.clear()
    
    #if the user submit the form
    if request.method == "POST":
        name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        PASSWORD_REGEX = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[?!@#$%^&*]).{8,}")
        if name and email and password and confirm and password == confirm and EMAIL_REGEX.match(email) and PASSWORD_REGEX.match(password):
            #add the user to the database
            try:
                new_user = users(user_name=name, user_email=email, master_pass=generate_password_hash(password), user_salt=secrets.token_bytes(32))
                db.session.add(new_user)
                db.session.commit()
                return redirect("/login")
            except IntegrityError:
                return apology("Email already exist")
        else:
            return apology("Wrong information")
    
    #render the register page
    return render_template("register.html")

#reset password
@app.route("/reset-pass", methods=["GET", "POST"])
def reset():
    #if the user submit the form
    if request.method == "POST":
        email = request.form.get("email")
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email and EMAIL_REGEX.match(email):
            #check if the user exist
            user = users.query.filter_by(user_email=email).first()
            if user:
                #send the reset password email
                token = secrets.token_urlsafe(32)
                reset_url = url_for("reset_password", token=token, _external=True)
                new_token = tokens(user_id=user.id, token=token)
                #add the token to the database
                db.session.add(new_token)
                msg = Message(
                    subject="CS:Pass Reset Password",
                    recipients=[email],
                    body= f"To reset your password pleas visit this link: {reset_url}\n attention all your passwords will be missed")
                #send the email
                mail.send(msg)
                db.session.commit()
                return redirect("/login")
            return apology("User not found")
        return apology("Wrong email")
    return render_template("reset.html")


@app.route('/reset-pass/<token>', methods=["GET", "POST"])
def reset_password(token):
    #if the user submit the form
    if request.method == "POST":
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        PASSWORD_REGEX = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[?!@#$%^&*]).{8,}")
        if password and confirm and password == confirm and PASSWORD_REGEX.match(password):
            #check if the token is valid
            user_token = tokens.query.filter_by(token=token).first()
            if user_token:
                #update the password
                user = users.query.filter_by(id=user_token.user_id).first()
                user.master_pass = generate_password_hash(password)
                db.session.delete(user_token)
                #delete all the user passwords because the password is changed and encryption key is lost
                passes_to_delete = passes.query.filter_by(user_id=user.id).all()
                for password in passes_to_delete:
                    db.session.delete(password)
                db.session.commit()
                return redirect("/login")
            else:
                return apology("acces denied")
        else:
            return apology("Wrong information")
    
    return render_template("resetpass.html", token=token)
    