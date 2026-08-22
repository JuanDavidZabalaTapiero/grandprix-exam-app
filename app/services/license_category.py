from app.core.decorators import handle_exceptions
from app.exceptions.license_category import (
    LicenseCategoryAlreadyExists,
    LicenseCategoryInUse,
    LicenseCategoryNotFound,
)
from app.extensions import db
from app.repositories.license_category import LicenseCategoryRepository


class LicenseCategoryService:
    @staticmethod
    @handle_exceptions
    def create(name):

        # Categoría ya registrada
        if LicenseCategoryRepository.get_by_name(name):
            raise LicenseCategoryAlreadyExists(name=name)

        category = LicenseCategoryRepository.create(name)
        db.session.commit()
        return category

    @staticmethod
    @handle_exceptions
    def get_by_id(id):
        return LicenseCategoryRepository.get_by_id(id)

    @staticmethod
    @handle_exceptions
    def get_all():
        return LicenseCategoryRepository.get_all()

    @staticmethod
    @handle_exceptions
    def update(category_id, name):
        category = LicenseCategoryRepository.get_by_id(category_id)

        # Categoría no encontrada
        if not category:
            raise LicenseCategoryNotFound(category_id=category_id)

        existing_category = LicenseCategoryRepository.get_by_name(name)

        # Categoría ya registrada
        if existing_category and existing_category.id != category_id:
            raise LicenseCategoryAlreadyExists(name=name)

        LicenseCategoryRepository.update(category, name)
        db.session.commit()
        return category

    @staticmethod
    @handle_exceptions
    def delete(category_id):
        category = LicenseCategoryRepository.get_by_id(category_id)

        # Categoría no encontrada
        if not category:
            raise LicenseCategoryNotFound(category_id=category_id)

        # Categoría vinculada a una matrícula
        if LicenseCategoryRepository.is_in_use(category_id):
            raise LicenseCategoryInUse(name=category.name)

        LicenseCategoryRepository.delete(category)
        db.session.commit()
