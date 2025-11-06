import json
from app.models.pokemon import Pokemon
from pathlib import Path

with open(Path("data/pokemon.json"), encoding="utf-8") as fichero:
    _POKEMONS = json.load(fichero)

def obtener_pokemons():
    pokemons = []
    for p in _POKEMONS:
        pokemon = Pokemon(**p)  #mete todo por clave valor, esto le pasa el diccionario entero, sino de puede id= p["id"]
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

#buscarpokemon por nombre
        
