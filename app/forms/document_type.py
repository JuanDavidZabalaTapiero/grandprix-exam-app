from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from .normalizers import normalize_text


class DocumentTypeForm(FlaskForm):
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
