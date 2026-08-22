from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.exceptions.database import DatabaseError
from app.exceptions.license_category import LicenseCategoryAlreadyExists
from app.services.license_category import LicenseCategoryService


def test_create_license_category(db_session):
    category = LicenseCategoryService.create("B1")
    assert category.name == "B1"
    assert category.id is not None


def test_create_license_category_duplicate_raises_error(db_session):
    LicenseCategoryService.create("B1")

    with pytest.raises(LicenseCategoryAlreadyExists):
        LicenseCategoryService.create("B1")


def test_create_raises_database_error_on_sqlalchemy_error(db_session):
    with (
        patch("app.services.license_category.db.session.commit") as mock_commit,
        patch("app.services.license_category.db.session.rollback") as mock_rollback,
    ):
        mock_commit.side_effect = SQLAlchemyError("Error simulado en base de datos")

        with pytest.raises(DatabaseError):
            LicenseCategoryService.create("B1")

        mock_rollback.assert_called_once()


def test_create_reraises_generic_exception(db_session):
    with (
        patch("app.services.license_category.db.session.commit") as mock_commit,
        patch("app.services.license_category.db.session.rollback") as mock_rollback,
    ):
        mock_commit.side_effect = Exception("Error inesperado del sistema")

        with pytest.raises(Exception) as excinfo:
            LicenseCategoryService.create("B1")

        assert str(excinfo.value) == "Error inesperado del sistema"

        mock_rollback.assert_called_once()


def test_get_all_returns_all_categories(db_session):
    LicenseCategoryService.create("A2")
    LicenseCategoryService.create("B1")

    categories = LicenseCategoryService.get_all()
    assert len(categories) == 2
    assert categories[0].name == "A2"
    assert categories[1].name == "B1"


def test_get_all_raises_database_error_on_sqlalchemy_error(db_session):
    with patch(
        "app.repositories.license_category.LicenseCategoryRepository.get_all"
    ) as mock_get_all:
        mock_get_all.side_effect = SQLAlchemyError("Error simulado en base de datos")

        with pytest.raises(DatabaseError):
            LicenseCategoryService.get_all()
