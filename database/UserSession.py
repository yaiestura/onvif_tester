from . import db


class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)



    def __repr__(self):
        pass