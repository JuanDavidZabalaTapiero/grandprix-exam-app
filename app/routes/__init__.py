from .api.document_type import document_type_api_bp
from .api.license_category import license_category_api_bp
from .web.core import core_bp
from .web.document_type import document_type_bp
from .web.license_category import license_category_bp


def register_blueprints(app):

    # HTML
    app.register_blueprint(core_bp)
    app.register_blueprint(license_category_bp)
    app.register_blueprint(document_type_bp)

    # API
    app.register_blueprint(license_category_api_bp)
    app.register_blueprint(document_type_api_bp)
