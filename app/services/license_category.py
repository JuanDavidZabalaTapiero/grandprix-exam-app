from app.core.decorators import handle_exceptions
from app.exceptions.license_category import (
    LicenseCategoryAlreadyExists,
    LicenseCategoryInUse,
    LicenseCategoryNotFound,
)
from app.extensions import db
from app.repositories.license_category import license_category_repository


class LicenseCategoryService:
    @staticmethod
    @handle_exceptions
    def create(name):

        # Categoría ya registrada
        if license_category_repository.get_by_name(name):
            raise LicenseCategoryAlreadyExists(name=name)

        category = license_category_repository.create(name=name)
        db.session.commit()
        return category

    @staticmethod
    @handle_exceptions
    def get_by_id(id):
        return license_category_repository.get_by_id(id)

    @staticmethod
    @handle_exceptions
    def get_all():
        return license_category_repository.get_all()

    @staticmethod
    @handle_exceptions
    def update(category_id, name):
        category = license_category_repository.get_by_id(category_id)

        # Categoría no encontrada
        if not category:
            raise LicenseCategoryNotFound(id=category_id)

        existing_category = license_category_repository.get_by_name(name)

        # Categoría ya registrada
        if existing_category and existing_category.id != category_id:
            raise LicenseCategoryAlreadyExists(name=name)

        license_category_repository.update(category, name)
        db.session.commit()
        return category

    @staticmethod
    @handle_exceptions
    def delete(category_id):
        category = license_category_repository.get_by_id(category_id)

        # Categoría no encontrada
        if not category:
            raise LicenseCategoryNotFound(id=category_id)

        # Categoría vinculada a una matrícula
        if license_category_repository.is_in_use(category_id):
            raise LicenseCategoryInUse(name=category.name)

        license_category_repository.delete(category)
        db.session.commit()
