from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class TrainerLoginForm(FlaskForm):
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

    contraseña = PasswordField("Contraseña", validators=[
        DataRequired(message="No has introducido una contraseña"),
        Length(min=4, max=20, message="La contraseña debe tener entre 4 y 20 caracteres")],
        render_kw={
            "placeholder": "Introduce contraseña"
    })

    enviar = SubmitField("Continuar",
                         render_kw={
                             "class": "submit"
                         })
