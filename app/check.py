from app import app, db
from models import Person

with app.app_context():
    print([f'{i};' for i in Person.query.all()])


