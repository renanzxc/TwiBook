from app import db 

class LikePost(db.Model):
  __tablename__ = "like_post"
  __table_args__ = (
    db.UniqueConstraint('liked_by', 'liked_post', name='unique_like'),
  )
  id = db.Column(db.Integer, primary_key=True)
  liked_by = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False) #FK
  liked_post = db.Column(db.Integer, db.ForeignKey('post.id'), unique=True, nullable=False) #FK

  user = db.relationship('User', backref='LikePost')
  user = db.relationship('Post', backref='LikePost')