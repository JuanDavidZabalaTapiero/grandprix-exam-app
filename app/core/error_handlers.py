import logging

from app.exceptions.base import AppError

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error):
        logger.warning(str(error))
        return {"message": str(error)}, error.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.critical(str(error))
        return {
            "message": "Ocurrió un error inesperado al procesar la operación en el servidor."
        }, 500
