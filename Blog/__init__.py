from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Admin1234@aa5sb5h1qmvgfh.cxy6d3sioze1.us-east-1.rds.amazonaws.com:5432/manage_user'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Blog import routes
from Blog import db

db.create_all()
