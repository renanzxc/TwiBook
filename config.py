import os
db_path = os.path.join(os.path.dirname(__file__), 'app.db')

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = True