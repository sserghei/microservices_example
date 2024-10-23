from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).one()

def init_db(app):
    db.init_app(app)  # Bind the database to the app