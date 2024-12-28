import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    symbols_price = {}
    symbols_price["total"] = user_info[0]["cash"]
    user_data = db.execute("SELECT * FROM data WHERE id = ?", session["user_id"])
    for symbol in user_data:
        symbols_price[symbol["symbol"]] = lookup(symbol["symbol"])["price"]
        symbols_price["total"] += symbols_price[symbol["symbol"]] * symbol["shares"]
    return render_template("index.html", user_info=user_info[0], user_data=user_data, symbols_price=symbols_price)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Invalid symbol")
        try:
            int(shares)
        except ValueError:
            return apology("Invalid shares")
        if not shares or int(shares) < 1:
            return apology("Invalid shares")
        shares = int(shares)
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol")
        user_shares = db.execute(
            "SELECT shares FROM data WHERE id = ? AND symbol = ?", session["user_id"], symbol)
        user_cash = int(db.execute("SELECT cash FROM users WHERE id = ?",
                        session["user_id"])[0]["cash"])
        if user_cash < quote["price"] * shares:
            return apology("To many shares")
        if user_shares == []:
            db.execute("INSERT INTO data (id, symbol, shares) VALUES(?, ?, ?)",
                       session["user_id"], symbol, shares)
        else:
            db.execute("UPDATE data SET shares = ? WHERE id = ? AND symbol = ?",
                       user_shares[0]["shares"] + shares, session["user_id"], symbol)
        user_cash = int(user_cash - quote["price"] * shares)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash, session["user_id"])
        db.execute("INSERT INTO history (id, symbol, shares, price, date) VALUES(?, ?, ?, ?, CURRENT_TIMESTAMP)",
                   session["user_id"], symbol, shares, quote["price"])
        flash("Bought!")
        return redirect("/")

    symbol = request.args.get("symbol")
    if symbol:
        return render_template("buy.html", symbol=symbol)
    return render_template("buy.html", symbol='')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_history = db.execute(
        "SELECT * FROM history WHERE id = ? ORDER BY date DESC", session["user_id"])
    return render_template("history.html", user_history=user_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username").lower()
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("No symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol")
        return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=quote["price"])

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("Missing username")
        elif not password:
            return apology("Missing password")
        elif password != confirmation:
            return apology("Password do not match")
        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                       username.lower(), generate_password_hash(password))
            return redirect("/login")
        except ValueError:
            return apology("Username not available")

    return render_template("register.html")


@app.route("/accont", methods=["GET", "POST"])
@login_required
def accont():
    """Change user password"""
    if request.method == "POST":
        old = request.form.get("old")
        cash = request.form.get("add")
        if old:
            new = request.form.get("new")
            if not new:
                return apology("New password Invalid")
            confirm = request.form.get("confirmation")
            if new != confirm:
                return apology("Password do not match")
            user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
            if not check_password_hash(user_info["hash"], old):
                return apology("Old password is wrong")
            db.execute("UPDATE users SET hash = ? WHERE id = ?",
                       generate_password_hash(new), session["user_id"])
            flash("Password has changed!")
            return redirect("/")
        elif cash:
            try:
                int(cash)
            except ValueError:
                return apology("Wrong amount of cash")
            cash = int(cash)
            if cash < 1:
                return apology("Wrong amount of cash")
            user_cash = db.execute("SELECT cash FROM users WHERE id = ?",
                                   session["user_id"])[0]["cash"]
            db.execute("UPDATE users SET cash = ?", user_cash + cash)
            flash("Cash added!")
            return redirect("/")
        else:
            return apology("Wrong request!")

    return render_template("accont.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Invalid symbol")
        user_symbol = db.execute(
            "SELECT * FROM data WHERE id = ? AND symbol = ?", session["user_id"], symbol)[0]
        if user_symbol == []:
            return apology("Invalid symbol")
        shares = request.form.get("shares")
        try:
            int(shares)
        except ValueError:
            return apology("Invalid shares")
        if not shares or int(shares) > user_symbol["shares"] or int(shares) < 1:
            return apology("Invalid shares")
        shares = int(shares)
        symbol_price = lookup(symbol)["price"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if user_symbol["shares"] == shares:
            db.execute("DELETE FROM data WHERE id = ? AND symbol = ?", session["user_id"], symbol)
        else:
            db.execute("UPDATE data SET shares = ? WHERE id = ? AND symbol = ?",
                       user_symbol["shares"] - shares, session["user_id"], symbol)
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   user_cash + shares * symbol_price, session["user_id"])
        db.execute("INSERT INTO history (id, symbol, shares, price, date) VALUES(?, ?, ?, ?, CURRENT_TIMESTAMP)",
                   session["user_id"], symbol, 0 - shares, symbol_price)
        flash("Sold!")
        return redirect("/")

    user_data = db.execute("SELECT * FROM data WHERE id = ?", session["user_id"])
    symbol = request.args.get("symbol")
    if symbol:
        return render_template("sell.html", user_data=user_data, sell_symbol=symbol)
    return render_template("sell.html", user_data=user_data, sell_symbol='')
