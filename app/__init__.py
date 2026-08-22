from flask import Flask

from .core.error_handlers import register_error_handlers
from .extensions import db, migrate
from .routes import register_blueprints


def create_app(config_class):

    app = Flask(__name__)

    # Config
    app.config.from_object(config_class)

    # Extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Modelos
    from .database import models  # noqa

    # Blueprints
    register_blueprints(app)

    # Errores
    register_error_handlers(app)

    return app
