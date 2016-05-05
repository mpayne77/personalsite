from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from passlib.hash import sha256_crypt

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')
    

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #attempted_username = request.form['username']
        #attempted_password = request.form['pasword']
        attempted_username = form.username.data
        attempted_password = form.password.data
        passcheck = sha256_crypt.verify(attempted_password,
            app.config['ADMIN_PASSWORD'])
        
        if attempted_username == app.config['ADMIN_USERNAME'] and passcheck:
            flash('You are logged in!')
            return redirect('index')
            
        else:
            flash('Login error')
            return render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', title='Sign In', form=form)
    

    