from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Field
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User, UserProfile

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError("That username is already taken. Please choose a different one")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError("That email is already taken. Please choose a different one")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ListField(Field):
    def process_formdata(self, valuelist):
        self.data = valuelistListField()
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    cv = FileField('CV', validators=[FileAllowed(['pdf'])])
    bio = TextAreaField('Bio')
    gmail = StringField('Gmail')
    github = StringField('Github')
    gitlab = StringField('Gitlab')
    facebook = StringField('Facebook')
    linkedln = StringField('Linkedln')
    instagram = StringField('Instagram')
    nouns = ListField()
    submit = SubmitField('Update')
  
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError("That username is already taken. Please choose a different one")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError("That email is already taken. Please choose a different one")

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')