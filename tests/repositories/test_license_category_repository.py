from app.repositories.license_category import license_category_repository
from app.services.license_category import LicenseCategoryService


def test_get_by_name_returns_category_when_exists(db_session):
    LicenseCategoryService.create("B1")

    result = license_category_repository.get_by_name("B1")

    assert result is not None
    assert result.name == "B1"


def test_get_by_name_returns_none_when_not_found(db_session):
    result = license_category_repository.get_by_name("B1")

    assert result is None


def test_get_all_return_empty_list_when_no_categories_exist(db_session):
    results = license_category_repository.get_all()

    assert results == []
    assert len(results) == 0


def test_get_all_returns_all_categories_sorted_by_name(db_session):
    LicenseCategoryService.create("C1")
    LicenseCategoryService.create("B1")
    LicenseCategoryService.create("A2")

    results = license_category_repository.get_all()

    assert len(results) == 3

    category_names = [category.name for category in results]
    assert category_names == ["A2", "B1", "C1"]
