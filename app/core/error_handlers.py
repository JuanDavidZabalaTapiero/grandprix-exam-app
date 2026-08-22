import logging

from flask import render_template

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.critical(str(error))
        return render_template("errors/500.html"), 500
