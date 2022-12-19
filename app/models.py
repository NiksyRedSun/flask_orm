from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    address = db.relationship('Address', backref='occupant', uselist=False)

    def __repr__(self):
        return f'Person id: {self.id}, named {self.name}, age {self.age}'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30))
    street = db.Column(db.String(30))
    house_number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __repr__(self):
        return f'{self.city}, {self.street}, {self.house_number}'
