from flask import Flask
import os
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager


app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='12345678'
db =SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category ='primary'
login_manager.session_protection = 'strong'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)


from app import views,form






