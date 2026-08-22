import pytest
from sqlalchemy.orm import sessionmaker

from app import create_app
from app.config import TestConfig
from app.extensions import db


@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app, db_session):
    return app.test_client()


@pytest.fixture
def req_ctx(app):
    with app.test_request_context() as ctx:
        yield ctx


@pytest.fixture(scope="function")
def db_session(app):
    connection = db.engine.connect()

    transaction = connection.begin()

    Session = sessionmaker(bind=connection, join_transaction_mode="create_savepoint")
    session = Session()

    original_session = db.session
    db.session = session

    try:
        yield session
    finally:
        session.close()
        db.session = original_session
        transaction.rollback()
        connection.close()
