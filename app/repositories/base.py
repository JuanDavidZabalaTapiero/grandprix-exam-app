from sqlalchemy import select

from app.extensions import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.session.add(instance)
        return instance

    def get_by_id(self, id):
        return db.session.get(self.model, id)

    def get_all(self):
        return db.session.scalars(select(self.model)).all()

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        return instance

    def delete(self, instance):
        db.session.delete(instance)
