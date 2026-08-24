import logging

from flask import render_template, request

from app.exceptions.base import AppError

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error):
        logger.warning(str(error))
        return {"message": str(error)}, error.status_code

    @app.errorhandler(404)
    def handle_not_found(error):
        logger.info(str(error))
        return render_template("errors/404.html"), 404

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.critical(str(error))
        if request.path.startswith("/api/"):
            return {
                "message": "Ocurrió un error inesperado al procesar la operación en el servidor."
            }, 500

        return render_template("errors/500.html"), 500
