from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    user_type = SelectField('User Type', choices=[('client', 'Client'), ('handyman', 'Handyman')],
                            validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    state = StringField('State', validators=[DataRequired()])
    full_name = StringField('Full Name', validators=[DataRequired()])
    about_yourself = TextAreaField('About Yourself', validators=[DataRequired()])
    occupation = StringField('Occupation')
    experience = StringField('Experience')
    submit = SubmitField('Register')
