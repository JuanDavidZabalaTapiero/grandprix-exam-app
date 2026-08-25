from app.core.decorators import handle_exceptions
from app.exceptions.document_type import (
    DocumentTypeAlreadyExists,
    DocumentTypeInUse,
    DocumentTypeNotFound,
)
from app.extensions import db
from app.repositories.document_type import document_type_repository


class DocumentTypeService:
    @staticmethod
    @handle_exceptions
    def create(name):

        # Tipo de documento ya registrado
        if document_type_repository.get_by_name(name):
            raise DocumentTypeAlreadyExists(name=name)

        document_type = document_type_repository.create(name=name)
        db.session.commit()
        return document_type

    @staticmethod
    @handle_exceptions
    def get_by_id(id):
        return document_type_repository.get_by_id(id)

    @staticmethod
    @handle_exceptions
    def get_all():
        return document_type_repository.get_all()

    @staticmethod
    @handle_exceptions
    def update(document_type_id, name):
        document_type = document_type_repository.get_by_id(document_type_id)

        # Tipo de documento no encontrado
        if not document_type:
            raise DocumentTypeNotFound(id=document_type_id)

        existing_document_type = document_type_repository.get_by_name(name)

        # Tipo de documento ya registrado
        if existing_document_type and existing_document_type.id != document_type_id:
            raise DocumentTypeAlreadyExists(name=name)

        document_type_repository.update(document_type, name=name)
        db.session.commit()
        return document_type

    @staticmethod
    @handle_exceptions
    def delete(document_type_id):
        document_type = document_type_repository.get_by_id(document_type_id)

        # Tipo de documento no encontrado
        if not document_type:
            raise DocumentTypeNotFound(id=document_type_id)

        # Tipo de documento vinculado a un estudiante
        if document_type_repository.is_in_use(document_type_id):
            raise DocumentTypeInUse(name=document_type.name)

        document_type_repository.delete(document_type)
        db.session.commit()
