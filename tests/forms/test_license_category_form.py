from werkzeug.datastructures import MultiDict

from app.forms.license_category import LicenseCategoryForm


def test_license_category_form_valid_data(req_ctx):
    data = MultiDict({"name": " b1  "})
    form = LicenseCategoryForm(data)

    assert form.validate() is True
    assert form.name.data == "B1"


def test_license_category_form_empty_name(req_ctx):
    data = MultiDict({"name": ""})
    form = LicenseCategoryForm(data)

    assert form.validate() is False


def test_license_category_form_name_too_short(req_ctx):
    data = MultiDict({"name": "b"})
    form = LicenseCategoryForm(data)

    assert form.validate() is False
    assert len(form.name.errors) > 0
