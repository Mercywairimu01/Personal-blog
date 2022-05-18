import os
import secrets
import requests
from flask_mail import Message
from app import mail
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt
from app.form import RegistrationForm, LoginForm,CommentForm,UpdateProfileForm,PostsForm, SubscriptionForm
from app.models import User, Post,Comment
from flask_login import login_user, current_user, logout_user, login_required




@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    random_quote_url ='http://quotes.stormconsultancy.co.uk/random.json'
    quote_response = requests.get(random_quote_url)
    quote_data = quote_response.json()
    posts=Post.query.order_by(Post.date_posted.desc())
    
    form = SubscriptionForm()
    if form.validate_on_submit():
        receivemail = form.email.data
        senderemail = mail
        msg = Message('Hey there.', sender=senderemail, recipients=receivemail)
        msg.html = '<h2>Welcome to Personal Blog.</h2> <p>This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.</p>'
        mail.send(msg)
        flash('You have been added to our subscription', 'success')
        return redirect(url_for('home'))
    return render_template('home.html',posts=posts,quote_data =quote_data)


@app.route("/about")
def about():
    return render_template('about.html',title ='About')



def save_avatar(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/photos', picture_fn)
    
    # resizing profile pic
    output_size =(130,130)
    i =Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn

@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    form =UpdateProfileForm()
    if form.validate_on_submit():
        if form.avatar.data:
            picture_file = save_avatar(form.avatar.data)
            current_user.avatar = picture_file
            
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated','success')
        return redirect(url_for('account'))
    elif request.method =='GET':
        form.email.data = current_user.email
        form.username.data = current_user.username
    avatar = url_for('static',filename='photos/' + current_user.avatar)
    return render_template('account.html',title ='Account',avatar=avatar,form =form)

@app.route("/register",  methods =['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created succefully,You can login now','success')
        return redirect(url_for('login'))
    return render_template('register.html',title ='Register',form =form)

@app.route("/login",  methods =['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
          login_user(user,remember=form.remember.data) 
          
          return redirect(request.args.get('next') or url_for('home'))  
        else:
   
          flash('Login not successfull.Please check username and password','danger')
    
    return render_template('login.html',title ='Login',form =form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/post/new',methods=['GET','post'])
@login_required
def new_post(): 
    form = PostsForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("post created",'success')
        return redirect(url_for('home')) 
    return render_template('new_posts.html',title ='New post',form =form)

@app.route('/<int:post_id>/', methods=('GET', 'POST'))
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment = Comment(content=request.form['content'], post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))

    return render_template('post.html', post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'post'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostsForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('new_posts.html', title='Update post',
                           form=form, legend='Update post')


@app.route("/post/<int:post_id>/delete", methods=['post'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
# ...

@app.route('/comments/')
def comments():
    form= CommentForm()
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template('comment.html', comments=comments ,form=form)

@app.post('/comments/<int:comment_id>/delete')
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))

@app.route("/subscribe")
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        receivemail = form.email.data
        msg = Message('Hey there.', recipients=receivemail)
        msg.html = '<h2>Welcome to Personal Blog.</h2> <p>Personal Blog is a  blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.</p>'
        mail.send(msg)
        flash('You have been added to our subscription', 'success')
        return redirect(url_for('home'))

    return redirect(url_for('home'))