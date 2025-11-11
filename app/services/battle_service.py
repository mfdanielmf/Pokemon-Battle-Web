import random
from app.services.pokemon_service import listar_pokemon


def random_moves(pokemon):
    movimientos = random.sample(pokemon.moves, min(4, len(pokemon.moves)))

    return movimientos


def random_pokemon():
    lista_pokemons = listar_pokemon()

    pokemon = random.choice(lista_pokemons)

    return pokemon


# para poder conseguir el atributo hp en el json data
def get_stat_value(pokemon, stat_name):
    for stat in pokemon.stats:
        if stat["name"] == stat_name:
            return stat["value"]
