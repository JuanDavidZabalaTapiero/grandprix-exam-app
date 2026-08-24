from flask import Blueprint

from app.services.document_type import DocumentTypeService

document_type_api_bp = Blueprint(
    "document_types_api", __name__, url_prefix="/api/document-types"
)


@document_type_api_bp.get("/")
def list():
    document_types = DocumentTypeService.get_all()
    return {
        "document_types": [
            {"id": doc_type.id, "name": doc_type.name} for doc_type in document_types
        ]
    }, 200


@document_type_api_bp.delete("/<int:document_type_id>")
def delete(document_type_id):
    DocumentTypeService.delete(document_type_id)
    return {"message": "Tipo de documento eliminado correctamente."}, 200
