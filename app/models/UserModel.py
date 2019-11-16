from app import db

class User(db.Model):
  __tablename__ = "user"
  __table_args__ = {'sqlite_autoincrement': True}
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), nullable=False, unique=True)
  password = db.Column(db.String(30), nullable=False)
  name = db.Column(db.String(30), nullable=False)
  description = db.Column(db.Text, nullable=False)
  numFollowers = db.Column(db.Integer, default=0)
  numFollowing = db.Column(db.Integer, default=0)

