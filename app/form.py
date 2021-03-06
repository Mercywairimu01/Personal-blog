from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password',message = 'Passwords must match')])
    submit = SubmitField('Sign up')
    
    def validate_username(self,username):
        user =User.query.filter_by(username = username.data).first()
        if user:
           raise ValidationError('Username is already taken')
   
    def validate_email(self,email):
        user =User.query.filter_by(email = email.data).first()
        if user:
           raise ValidationError('Email is already taken')
   
   
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember= BooleanField('Remember Me')
	login = SubmitField('Sign In')
 
class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    avatar=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user =User.query.filter_by(username = username.data).first()
            if user:
               raise ValidationError('Username is already taken')
   
    def validate_email(self,email):
        if email.data != current_user.email:
            user =User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email is already taken') 


class CommentForm(FlaskForm):
    content = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment') 
    

class PostsForm(FlaskForm):
    title =StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()]) 
    submit = SubmitField('Post')  
    
class SubscriptionForm(FlaskForm):
    email = StringField('Subscribe to our email Newsletter',validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')    
       