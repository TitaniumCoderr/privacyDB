from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired,Email


class checkLeakForm(FlaskForm):
    email = EmailField("Email",[DataRequired(),Email()],render_kw={"placeholder":"Enter Email"})
    passwrd=PasswordField("Password", [DataRequired()],render_kw={"placeholder":"Enter Password"})
    submit=SubmitField("<< CHECK NOW >>")



