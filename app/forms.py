from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextField
#from wtforms.validators import DataRequired
from wtforms import validators

    
class LoginForm(Form):
    #username = StringField('Username', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class CreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200,
        message='Title must be between 1 and 200 characters!')])
    subtitle = StringField('Subtitle', [validators.Length(min=0, max=200,
        message='Subtitle may not exceed 200 characters')])
    content = TextField('Content', [validators.Length(min=1,
        message='You need to enter some content dummy!')])
        
    