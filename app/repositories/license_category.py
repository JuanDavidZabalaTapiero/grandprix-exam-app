from sqlalchemy import select

from app.database.models import Enrollment, LicenseCategory
from app.extensions import db

from .base import BaseRepository


class LicenseCategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(LicenseCategory)

    def get_by_name(self, name):
        return db.session.execute(
            select(LicenseCategory).where(LicenseCategory.name == name)
        ).scalar_one_or_none()

    def is_in_use(self, category_id):
        return (
            db.session.execute(
                select(Enrollment.id)
                .where(Enrollment.license_category_id == category_id)
                .limit(1)
            ).first()
            is not None
        )


license_category_repository = LicenseCategoryRepository()
