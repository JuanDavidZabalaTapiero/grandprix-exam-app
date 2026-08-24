from sqlalchemy import select

from app.database.models import DocumentType, Student
from app.extensions import db


class DocumentTypeRepository:
    @staticmethod
    def create(name):
        document_type = DocumentType(name=name)
        db.session.add(document_type)
        return document_type

    @staticmethod
    def get_by_id(id):
        return db.session.get(DocumentType, id)

    @staticmethod
    def get_by_name(name):
        return db.session.execute(
            select(DocumentType).where(DocumentType.name == name)
        ).scalar_one_or_none()

    @staticmethod
    def get_all():
        return db.session.scalars(
            select(DocumentType).order_by(DocumentType.name)
        ).all()

    @staticmethod
    def is_in_use(document_type_id):
        return (
            db.session.execute(
                select(Student.id)
                .where(Student.document_type_id == document_type_id)
                .limit(1)
            ).first()
            is not None
        )

    @staticmethod
    def update(document_type, name):
        document_type.name = name
        return document_type

    @staticmethod
    def delete(document_type):
        db.session.delete(document_type)
