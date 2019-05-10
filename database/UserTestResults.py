from . import db


class UserTestResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        pass