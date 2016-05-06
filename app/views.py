from flask import render_template, flash, redirect, url_for
from app import app, models
from .forms import LoginForm
from passlib.hash import sha256_crypt


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html')


@app.route('/')
@app.route('/home/')
def home():
    posts = models.BlogPost.query.all()
    return render_template('home.html', posts=posts)
    

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
            return redirect(url_for('home'))
            
        else:
            flash('Login error')
            return render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', title='Sign In', form=form)
    

    