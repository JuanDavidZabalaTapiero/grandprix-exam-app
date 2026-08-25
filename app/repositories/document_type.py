from sqlalchemy import select

from app.database.models import DocumentType, Student
from app.extensions import db

from .base import BaseRepository


class DocumentTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(DocumentType)

    def get_by_name(self, name):
        return db.session.execute(
            select(DocumentType).where(DocumentType.name == name)
        ).scalar_one_or_none()

    def is_in_use(self, document_type_id):
        return (
            db.session.execute(
                select(Student.id)
                .where(Student.document_type_id == document_type_id)
                .limit(1)
            ).first()
            is not None
        )


document_type_repository = DocumentTypeRepository()
