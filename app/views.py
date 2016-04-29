from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Matt'}
    posts = [
        {
            'author': {'username': 'Matt'},
            'body': 'This is the first post!'
        },
        {
            'author': {'username': 'Matt'},
            'body': 'This is the 2nd post! Sup bro?'
        }
            
    ]
    return render_template('home.html', title = 'Home',
                            user=user, posts=posts)
    
    
    
