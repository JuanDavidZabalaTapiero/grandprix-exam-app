from .base import AppError


class DocumentTypeError(AppError):
    pass


class DocumentTypeNotFound(DocumentTypeError):
    default_message = "El tipo de documento con id {id} no existe."
    status_code = 404


class DocumentTypeAlreadyExists(DocumentTypeError):
    default_message = "El tipo de documento '{name}' ya está registrado."
    status_code = 409


class DocumentTypeInUse(DocumentTypeError):
    default_message = "El tipo de documento '{name}' tiene estudiantes asociados y no puede eliminarse."
    status_code = 409
