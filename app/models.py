from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin ,db.Model):
    
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(150), unique=True, nullable=False)
   bio = db.Column(db.String(255))
   avatar = db.Column(db.String(80),nullable = False, default ='default.jpg')
   password =db.Column(db.String(255),nullable =False)
   posts = db.relationship('Post', backref='author', lazy='dynamic')
   
   
   def save_user(self):
       db.session.add(self)
       db.session.commit()
   def __repr__(self) :
        return f"User('{self.username}','{self.email}','{self.avatar}'"

class Post(db.Model):
  
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    content =db.Column(db.Text(255),nullable = False)
    comments = db.relationship('Comment', backref='post', lazy='dynamic') 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable =False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
   
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable = False)
    
  
    def __repr__(self):
        return f"Comment('{self. content[:20]}')"


