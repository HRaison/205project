from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email Address', validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PaymentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    credit_type = SelectField('Credit Card Type', validators=[DataRequired()],
                            choices=[('visa', 'visa'),
                                    ('jcb', 'jcb'),
                                    ('master', 'master')])
    credit_no = IntegerField('Credit Card Number', validators=[DataRequired(), NumberRange(min=1000000000000000, max=9999999999999999)])
    expir_month = SelectField('Expiry Month', validators=[DataRequired()],
                            choices=[('1', '1'),
                                    ('2', '2'),
                                    ('3', '3'),
                                    ('4', '4'),
                                    ('5', '5'),
                                    ('6', '6'),
                                    ('7', '7'),
                                    ('8', '8'),
                                    ('9', '9'),
                                    ('10', '10'),
                                    ('11', '11'),
                                    ('12', '12')])
    expir_year = SelectField('Expiry Year', validators=[DataRequired()],
                            choices=[('2020', '2020'),
                                    ('2021', '2021'),
                                    ('2022', '2022'),
                                    ('2023', '2023'),
                                    ('2024', '2024'),
                                    ('2025', '2025')])
    cvv = IntegerField('CVV', validators=[DataRequired(), NumberRange(min=100, max=999)])
    money = IntegerField('Donate Value (in HKD)', validators=[DataRequired()])
    animal_name = SelectField('Chose the animal that you want to donate', validators=[DataRequired()],
                            choices=[('Doe', 'Doe'),
                                    ('SoSo', 'SoSo'),
                                    ('QQ', 'QQ'),
                                    ('Judy', 'Judy'),
                                    ('Rex', 'Rex'),
                                    ('GT', 'GT')])
    submit = SubmitField('Submit')

class FeedbackForm(FlaskForm):
    rating = IntegerField('Rating (1 for the worst, 10 for the best)', validators=[NumberRange(min=1, max=10, message='1 for the worst, 10 for the best')])
    feed_type = SelectField('Feedback Type', validators=[DataRequired()],
                            choices=[('Comments', 'comments'),
                                    ('Questions', 'questions'),
                                    ('Reports', 'reports')])
    comment = TextAreaField('Write something here', validators=[DataRequired()])
    feed_email = StringField('Email Address', validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField('Submit')


class AnimalForm(FlaskForm):
    animal_name = StringField('Animal Name', validators=[DataRequired()])
    years_old = IntegerField('Years old', validators=[DataRequired(), NumberRange(min=1, max=99)])
    disease = StringField('Disease', validators=[DataRequired()])
    submit = SubmitField('Submit')
