from sqlalchemy import select

from app.database.models import Enrollment, LicenseCategory
from app.extensions import db


class LicenseCategoryRepository:
    @staticmethod
    def create(name):
        category = LicenseCategory(name=name)
        db.session.add(category)
        return category

    @staticmethod
    def get_by_id(id):
        return db.session.get(LicenseCategory, id)

    @staticmethod
    def get_by_name(name):
        return db.session.execute(
            select(LicenseCategory).where(LicenseCategory.name == name)
        ).scalar_one_or_none()

    @staticmethod
    def get_all():
        return db.session.scalars(
            select(LicenseCategory).order_by(LicenseCategory.name)
        ).all()

    @staticmethod
    def is_in_use(category_id):
        return (
            db.session.execute(
                select(Enrollment.id)
                .where(Enrollment.license_category_id == category_id)
                .limit(1)
            ).first()
            is not None
        )

    @staticmethod
    def update(category, name):
        category.name = name
        return category

    @staticmethod
    def delete(category):
        db.session.delete(category)
