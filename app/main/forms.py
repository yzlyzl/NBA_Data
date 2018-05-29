from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Required


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

#登录表单
class Login_Form(FlaskForm):
    name=StringField('name',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()])
    submit=SubmitField('Login in')


#注册表单
class Register_Form(FlaskForm):
    name=StringField('name',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()])
    submit=SubmitField('register')

