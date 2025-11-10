from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokemonSelectForm(FlaskForm):
    pokemon = StringField(
        validators=[DataRequired(
            message="No has introducido un pokemon válido")],
        render_kw={
            "placeholder": "Introduce el nombre de un pokemon",
            "id": "default-search",
            "class": "block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
        })

    enviar = SubmitField("Seleccionar",
                         render_kw={
                             "class": "text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 hover:cursor-pointer focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2"
                         })
