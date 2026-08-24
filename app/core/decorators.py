import functools
import logging

from app.exceptions.base import AppError
from app.extensions import db

logger = logging.getLogger(__name__)


def handle_exceptions(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except AppError:
            db.session.rollback()
            raise

        except Exception as e:
            db.session.rollback()
            logger.critical(str(e))
            raise

    return wrapper
