from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextField, FileField, TextAreaField, SubmitField
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
    thumbnail = FileField('Thumbnail')
    content = TextAreaField('Content', 
        [validators.Required('You need to enter some content!')])
    author = StringField('Author', [validators.Length(min=1, 
        message='You need to enter an author!')])
    published = BooleanField()
    submit = SubmitField('Save')
    
        
    