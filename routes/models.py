from flask_sqlalchemy import SQLAlchemy
from app import db


class Handyman(db.Model):
    __tablename__ = 'Handyman'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    about_yourself = db.Column(db.Text, nullable=False)
    occupation = db.Column(db.String(100))
    experience = db.Column(db.String(100))

    def __init__(self, email, username, password, user_type, state, full_name, about_yourself, occupation=None,
                 experience=None):
        self.email = email
        self.username = username
        self.password = password
        self.user_type = user_type
        self.state = state
        self.full_name = full_name
        self.about_yourself = about_yourself
        self.occupation = occupation
        self.experience = experience
