from app import db 

class Post(db.Model):
  __tablename__ = "post"

  id = db.Column(db.Integer, primary_key=True)
  created_by = db.Column(db.Integer, db.ForeignKey('user.id')) #FK
  title = db.Column(db.String(30), nullable=False)
  text = db.Column(db.Text, nullable=False)
  num_likes = db.Column(db.Integer, default=0)
  num_comments = db.Column(db.Integer, default=0)
  
  user = db.relationship('User', backref='post')