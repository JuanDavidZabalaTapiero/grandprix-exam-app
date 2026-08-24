from flask import Blueprint, flash, redirect, render_template, url_for

from app.exceptions.base import AppError
from app.forms.document_type import DocumentTypeForm
from app.services.document_type import DocumentTypeService

document_type_bp = Blueprint("document_types", __name__, url_prefix="/document-types")


@document_type_bp.get("/")
def list():
    return render_template("document_type/list.html")


@document_type_bp.route("/register", methods=["GET", "POST"])
def create():
    form = DocumentTypeForm()

    if form.validate_on_submit():
        name = form.name.data

        # Servicio
        try:
            DocumentTypeService.create(name)
            flash("Tipo de documento registrado correctamente.", "success")
            return redirect(url_for("document_types.list"))
        except AppError as e:
            flash(str(e), "danger")

    return render_template("document_type/create.html", form=form)


@document_type_bp.route("<int:document_type_id>/edit", methods=["GET", "POST"])
def update(document_type_id):
    document_type = DocumentTypeService.get_by_id(document_type_id)

    form = DocumentTypeForm(obj=document_type)

    if form.validate_on_submit():
        name = form.name.data

        # Servicio
        try:
            DocumentTypeService.update(document_type_id, name)
            flash("Tipo de documento actualizado correctamente.", "success")
            return redirect(url_for("document_types.list"))
        except AppError as e:
            flash(str(e), "danger")

    return render_template("document_type/edit.html", form=form)
