from app import db 

class Comment(db.Model):
  __tablename__ = "comment"

  id = db.Column(db.Integer, primary_key=True)
  created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  of = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
  text = db.Column(db.Text, nullable=False)

  user = db.relationship('User', backref='comment')
  post = db.relationship('Post', backref='comment')
