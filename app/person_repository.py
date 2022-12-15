from dataclasses import dataclass
from person_exceptions import PersonException
from app import app, db
from models import Person


class person_repository:

    def __guard_is_not_empty(self, person):
        if person is None:
            raise ValueError('There was no any person')

    def get(self, person=None):
        with app.app_context():
            if person is not None:
                result = Person.query.get(person.id)
                if result is None:
                    raise PersonException(f'Person with id {person.id} not found')
                else:
                    return str(result)
            else:
                return [str(i) for i in Person.query.all()]

    def delete(self, person):
        self.__guard_is_not_empty(person)
        try:
            with app.app_context():
                db.session.delete(Person.query.get(person.id))
                db.session.commit()
                return True
        except:
            raise PersonException('Не удалось выполнить запрос')

    def create(self, person):
        self.__guard_is_not_empty(person)
        with app.app_context():
            result_person = Person(name=person.name, age=person.age)
            db.session.add(result_person)
            db.session.commit()
            return f'Current Person id is {result_person.id}'

    def update(self, person):
        self.__guard_is_not_empty(person)
        with app.app_context():
            current_person = Person.query.get(person.id)
            if current_person:
                current_person.name = person.name
                current_person.age = person.age
                db.session.commit()
                return True
            else:
                raise PersonException(f'Person with id {person.id} not found')
