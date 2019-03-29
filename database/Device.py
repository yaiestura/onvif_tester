class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    ip = db.Column(db.String(60), unique=True, nullable=False)
    port = db.Column(db.String(40), nullable=False)
    login = db.Column(db.String(60), nullable=False, default='admin')
    password = db.Column(db.String(30), nullable=False, default='Supervisor')
    deviceinfo = db.Column(db.Text, nullable=True)
    features = db.relationship('Features')

    def __repr__(self):
        return f"Device('{self.type}', '{self.name}', '{self.ip}',
        '{self.port}', '{self.login}', '{self.password}', '{self.deviceinfo}')"