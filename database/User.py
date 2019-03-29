from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(40), nullable=True)
    surname = db.Column(db.String(60), nullable=True)
    image_url = db.Column(db.String(30), nullable=False, default='default.jpg')
    register_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}',
        '{self.name}', '{self.surname}', '{self.image_url}', '{self.register_date}')"
