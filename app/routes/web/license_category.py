from flask import Blueprint, flash, redirect, render_template, url_for

from app.exceptions.base import AppError
from app.forms.license_category import LicenseCategoryForm
from app.services.license_category import LicenseCategoryService

license_category_bp = Blueprint(
    "license_categories", __name__, url_prefix="/license-categories"
)


@license_category_bp.get("/")
def list():
    return render_template("license_category/list.html")


@license_category_bp.route("/register", methods=["GET", "POST"])
def create():
    form = LicenseCategoryForm()

    if form.validate_on_submit():
        name = form.name.data

        # Servicio
        try:
            LicenseCategoryService.create(name)
            flash("Categoría registrada correctamente.", "success")
            return redirect(url_for("license_categories.list"))
        except AppError as e:
            flash(str(e), "danger")

    return render_template("license_category/create.html", form=form)


@license_category_bp.route("/<int:category_id>/edit", methods=["GET", "POST"])
def update(category_id):
    category = LicenseCategoryService.get_by_id(category_id)

    form = LicenseCategoryForm(obj=category)

    if form.validate_on_submit():
        name = form.name.data

        # Servicio
        try:
            LicenseCategoryService.update(category_id, name)
            flash("Categoría actualizada correctamente.", "success")
            return redirect(url_for("license_categories.list"))
        except AppError as e:
            flash(str(e), "danger")

    return render_template("license_category/edit.html", form=form)
