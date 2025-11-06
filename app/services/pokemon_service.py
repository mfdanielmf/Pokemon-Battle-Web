import app.repositories.pokemon_repo as pokemon_repo


def listar_pokemon():
    return pokemon_repo.obtener_pokemons()


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None  # o lanzar una excepcion
    return pokemon_repo.buscar_por_id(id)


def pokemon_existe(nombre):
    lista_pokemons = listar_pokemon()

    for p in lista_pokemons:
        if p.name.lower() == nombre.lower():
            return p

    return False

# gacer la logica de buscar copkemon para combatir
