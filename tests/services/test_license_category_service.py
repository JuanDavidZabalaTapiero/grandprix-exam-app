from unittest.mock import patch

import pytest

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
