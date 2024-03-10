from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired,Email


class checkLeakForm(FlaskForm):
    email = EmailField("Email",[DataRequired(),Email()])
    passwrd=PasswordField("Password", [DataRequired()])
    submit=SubmitField("Check")



