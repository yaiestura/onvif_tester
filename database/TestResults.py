from . import db


class TestResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)



    def __repr__(self):
        pass