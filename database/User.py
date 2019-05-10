from datetime import datetime
from flask_login.mixins import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(40), nullable=True)
    surname = db.Column(db.String(60), nullable=True)
    image_url = db.Column(db.String(30), nullable=False, default='default.jpg')
    register_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)


    def get_id(self):
        return str(self.id)


    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password , password)


    def __repr__(self):
        return "User(%d)" % id
