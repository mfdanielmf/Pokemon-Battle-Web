import json
from app.models.pokemon import Pokemon
from pathlib import Path

DIRECTORIO_BASE = Path(__file__).resolve().parent.parent.parent
DATA_POKEMON = DIRECTORIO_BASE.joinpath("data", "pokemon.json")

with open(DATA_POKEMON, encoding="utf-8") as fichero:
    _POKEMONS = json.load(fichero)


def obtener_pokemons():
    pokemons = []
    for p in _POKEMONS:
        # mete todo por clave valor, esto le pasa el diccionario entero, sino de puede id= p["id"]
        pokemon = Pokemon(**p)
        pokemons.append(pokemon)
    return pokemons


def buscar_por_id(id):
    pokemons = obtener_pokemons()
    pokemon_a_buscar = None
    for p in pokemons:
        if p.id == id:
            pokemon_a_buscar = p
            break
    return pokemon_a_buscar


def buscar_por_nombre(nombre):
    lista_pokemons = obtener_pokemons()

    for p in lista_pokemons:
        if p.name.lower() == nombre.lower():
            return p
