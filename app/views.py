from flask import render_template, flash, redirect, url_for, request
from app import app, models, db
from .forms import LoginForm, CreateForm
from passlib.hash import sha256_crypt
from datetime import datetime



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash('Error in the %s field - %s' % (
                getattr(form, field).label.text, error))


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html')


@app.route('/')
@app.route('/home/')
def home():
    posts = models.BlogPost.query.order_by(models.BlogPost.timestamp.desc()).all()
    return render_template('home.html', posts=posts)
    

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
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
    

@app.route('/create/', methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            newpost = models.BlogPost()
            newpost.title = request.form.get('title')
            newpost.subtitle = request.form.get('subtitle')
            newpost.content = request.form.get('content')
            newpost.author = request.form.get('author')
            newpost.timestamp = datetime.now()
            
            if request.form.get('published') == 'y':
                newpost.published = True
            else:
                newpost.published = False
            #newpost.published = request.form.get('published')
            db.session.add(newpost)
            db.session.commit()
            
            flash('New entry posted')
            return redirect(url_for('home'))
        else:
            flash_errors(form)
            return redirect(url_for('create'))
    else:
        return render_template('create.html', form=form)
    
    