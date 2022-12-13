from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    address = db.relationship('Address', backref='occupant', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30))
    street = db.Column(db.String(30))
    house_number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.city}, {self.street}, {self.house_number}'
