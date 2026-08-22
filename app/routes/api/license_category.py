from flask import Blueprint

from app.exceptions.base import AppError
from app.services.license_category import LicenseCategoryService

license_category_api_bp = Blueprint(
    "license_categories_api", __name__, url_prefix="/api/license-categories"
)


@license_category_api_bp.get("/")
def list():
    categories = LicenseCategoryService.get_all()

    return {
        "categories": [
            {"id": category.id, "name": category.name} for category in categories
        ]
    }, 200


@license_category_api_bp.delete("/<int:category_id>")
def delete(category_id):
    try:
        LicenseCategoryService.delete(category_id)

        return {"message": "Categoría eliminada correctamente."}, 200

    except AppError as e:
        return {"message": str(e)}, e.status_code
