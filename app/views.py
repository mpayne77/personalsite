from app import app, models
from flask import (render_template, flash, redirect, url_for, request)
from peewee import *
from playhouse.flask_utils import get_object_or_404


@app.before_request
def before_request():
    db = models.mysql_db
    db.connect()
    
    
@app.after_request
def after_request(response):
    db = models.mysql_db
    db.close()
    return response
    

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
                            
                            
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
   
    
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            blogpost = models.Blogpost.create(
                title = request.form['title'],
                content=request.form['content'],
                thumbnail = request.form['thumbnail'],
                published = request.form.get('published') or False)
            blogpost.save()
            flash('Blog post created successfully.', 'success')
            
            if blogpost.published:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('edit', slug=blogpost.slug))
                
        else:
            flash('Title and Content are required.', 'danger')
            
    return render_template('create.html')
    
    
@app.route('/<slug>/edit', methods=['GET', 'POST'])
def edit(request, slug):
    if request.method == 'POST':
        blogpost = get_object_or_404(models.Blogpost, models.Blogpost.slug == slug)
        if request.form.get('title') and request.form.get('content'):
            blogpost = models.Blogpost.create(
                title = request.form['title'],
                content=request.form['content'],
                thumbnail = request.form['thumbnail'],
                published = request.form.get('published') or False)
            blogpost.save()
            flash('Blog post created successfully.', 'success')
            
            if blogpost.published:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('edit', slug=blogpost.slug))
                
        else:
            flash('Title and Content are required.', 'danger')
            
    return render_template('create.html')  

            

    