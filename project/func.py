from flask import redirect, render_template, session
from functools import wraps

#import libraries for encryption got it from chatgpt
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64


def encrypt(data, user_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(user_key))
    crypter = Fernet(key)
    encrypted = crypter.encrypt(data.encode())
    return encrypted

def decrypt(data, user_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(user_key))
    crypter = Fernet(key)
    decrypted = crypter.decrypt(data).decode()
    return decrypted


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def fixdomain(domain):
    domain = domain.rsplit('.', 1)[0]
    if len(domain) > 12:
        return domain[:12] + '...'
    return domain


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("error.html", top=code, bottom=escape(message)), code

