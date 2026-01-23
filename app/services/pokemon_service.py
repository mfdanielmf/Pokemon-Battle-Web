import app.repositories.pokemon_repo as pokemon_repo
from app.clients.pokemon_client import fetch_pokemon_parallel, fetch_moves_parallel, PokemonClient

pokemon_client = PokemonClient()

def listar_pokemon():
    return pokemon_repo.obtener_pokemons()


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None
    return pokemon_repo.buscar_por_id(id)


def obtener_pokemon_por_nombre(nombre):
    return pokemon_repo.buscar_por_nombre(nombre)


def adaptar_pokemon(data):
    data_return = []
    for pokemon in data:
        height = pokemon["height"]
        id = pokemon["id"]
        name = pokemon["name"]

        stats = []
        for stat_actual in pokemon["stats"]:
            nombre_stat = stat_actual["stat"]["name"]
            if nombre_stat == "hp":
                stats.append({
                    "name": "hp",
                    "value": stat_actual["base_stat"]
                })
            if nombre_stat == "attack":
                stats.append({
                    "name": "attack",
                    "value": stat_actual["base_stat"]
                })
            if nombre_stat == "defense":
                stats.append({
                    "name": "defense",
                    "value": stat_actual["base_stat"]
                })
            if nombre_stat == "special-attack":
                stats.append({
                    "name": "special-attack",
                    "value": stat_actual["base_stat"]
                })
            if nombre_stat == "special-defense":
                stats.append({
                    "name": "special-defense",
                    "value": stat_actual["base_stat"]
                })
            if nombre_stat == "speed":
                stats.append({
                    "name": "speed",
                    "value": stat_actual["base_stat"]
                })

        sprites = {
            "front_default": pokemon["sprites"]["front_default"],
            "back_default": pokemon["sprites"]["back_default"],
            "front_shiny": pokemon["sprites"]["front_shiny"],
            "back_shiny": pokemon["sprites"]["back_shiny"]
        }

        types = []
        for tipo in pokemon["types"]:
            types.append(tipo["type"]["name"])

        weight = pokemon["weight"]

       
        data_pokemon = {
            "height": height,
            "id": id,
            "name": name,
            "stats": stats,
            "sprites": sprites,
            "types": types,
            "weight": weight,
        }

        data_return.append(data_pokemon)

    return data_return

def adaptar_moves(data, pokemonSinMove):
    linkMoves = []
    for move_actual in data["moves"]:
        linkMoves.append(move_actual["move"]["url"])
        if (len(linkMoves) > 9):
            break


    movesPokemon = fetch_moves_parallel(linkMoves, pokemon_client)
        
    moves = []
    for move in movesPokemon:
        nombreMovimiento = move["name"]
        accuracyMovimiento = move["accuracy"]
        powerMovimiento = move["power"]
        typeMovimiento = move["type"]["name"]

        if (accuracyMovimiento is None):
            accuracyMovimiento = 100

        if powerMovimiento is None:
            powerMovimiento = 50

        moves.append({
            "name": nombreMovimiento,
            "accuracy": accuracyMovimiento,
            "power": powerMovimiento,
            "type": typeMovimiento
        })
    
    
    pokemonSinMove[0]["moves"] = moves
    
    return pokemonSinMove


# def validar_pokemon(data):
#     if data["id"] not in data or "name" not in data:
#         return False
#     return True



urls = [
    383,
    382,
    483,
    487,
    484
]

def obtener_pokemon_adaptado():
    data = fetch_pokemon_parallel(urls, pokemon_client)

    if data is None:
        return None

    # if not validar_pokemon(data):
    #     return None

    pokemon = adaptar_pokemon(data)

    return pokemon

def obtener_pokemon_por_id_client(id):
    data = pokemon_client.fetch_pokemon_detail(id)
    
    pokemonSinMove = adaptar_pokemon([data])
    pokemon = adaptar_moves(data, pokemonSinMove)
    return pokemon[0]
