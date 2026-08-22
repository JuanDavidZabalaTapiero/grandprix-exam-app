import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


def normalize_text(value):
    if value:
        value = value.strip()
        value = re.sub(r"\s+", " ", value)
        return value.upper()
    return value


class LicenseCategoryForm(FlaskForm):
    name = StringField(
        label="Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(
                min=2,
                max=50,
                message="El nombre debe tener mínimo 2 caracteres y máximo 50.",
            ),
        ],
        filters=[normalize_text],
    )
    submit = SubmitField(label="Registrar")
