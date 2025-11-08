import random
from app.services.pokemon_service import pokemon_existe

# hacer le buscaodor de random pokemon y enemigo igual q su imgen


def random_moves(nombre):
    pokemon = pokemon_existe(nombre)

    movimientos = random.sample(
        pokemon.moves, min(4, len(pokemon.moves)))

    return movimientos
