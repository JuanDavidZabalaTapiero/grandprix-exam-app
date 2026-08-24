from .base import AppError


class LicenseCategoryError(AppError):
    pass


class LicenseCategoryNotFound(LicenseCategoryError):
    default_message = "La categoría con id {category_id} no existe."
    status_code = 404


class LicenseCategoryAlreadyExists(LicenseCategoryError):
    default_message = "La categoría '{name}' ya está registrada."
    status_code = 409


class LicenseCategoryInUse(LicenseCategoryError):
    default_message = (
        "La categoría '{name}' tiene matrículas vinculadas y no puede eliminarse."
    )
    status_code = 409
