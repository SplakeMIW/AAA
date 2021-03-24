from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)