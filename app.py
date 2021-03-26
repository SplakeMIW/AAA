from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, abort
from models import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def homepage():
    users = User.query.all()
    return print(users)