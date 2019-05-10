from . import db
from datetime import datetime

class TestResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship("Device", backref="reports")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="reports")
    created = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    url = db.Column(db.String(256), nullable=False)

