from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    uid = StringField("uid",validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    dob = StringField("date of birth",validators=[DataRequired()])
    phone = StringField("phone",validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    budget = StringField("budget",validators=[DataRequired()])
    account = StringField("account",validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class BlogForm(FlaskForm):
    username = SelectField('Username', choices=[], coerce=int)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class CarInfoForm(FlaskForm):
    username = SelectField('Username', choices=[], coerce=int)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    carType = StringField('Car Type', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    manuYear = StringField('Manu Year', validators=[DataRequired()]) 
    specialist = SelectField('Specialist', choices=[], coerce=int)
    stars = SelectField('Stars', choices=[], coerce=int)
    image = StringField('Image ID', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

    
        
