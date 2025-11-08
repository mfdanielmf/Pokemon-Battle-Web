from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class TrainerForm(FlaskForm):
    entrenador = StringField("Entrenador", validators=[
                             DataRequired(
                                 message="No has introducido un entrenador"),
                             Length(
                                 min=3, max=15, message="Debe tener entre 3 y 15 caracteres"),
                             Regexp(r'^[A-Za-z0-9_]+$', message="Solo se permiten letras, números y _")],

                             render_kw={
        "placeholder": "Introduce nombre",
        "pattern": "^[A-Za-z0-9_]+$"
    })

    enviar = SubmitField("Continuar",
                         render_kw={
                             "class": "submit"
                         })
