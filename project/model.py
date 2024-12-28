from app import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, unique=True, nullable=False)
    master_pass = db.Column(db.String, nullable=False)
    user_salt = db.Column(db.String, unique=True, nullable=False)
    

class passes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(users.id), nullable=False)
    domain = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    
class tokens(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(users.id))
    token = db.Column(db.String, primary_key=True)
