import app.repositories.pokemon_repo as pokemon_repo
from app.clients.pokemon_client import fetch_pokemon_parallel, fetch_moves_parallel

def listar_pokemon():
    return pokemon_repo.obtener_pokemons()


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None
    return pokemon_repo.buscar_por_id(id)


def obtener_pokemon_por_nombre(nombre):
    return pokemon_repo.buscar_por_nombre(nombre)


def adaptar_pokemon(data):
    height = data["height"]
    id = data["id"]
    name = data["name"]

    stats = []
    for stat_actual in data["stats"]:
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

    sprites = []
    sprites.append({
        "front_default": data["sprites"]["front_default"]
        })
    sprites.append({
        "back_default": data["sprites"]["back_default"]
        })
    sprites.append({
        "front_shiny": data["sprites"]["front_shiny"]
        })
    sprites.append({
        "back_shiny": data["sprites"]["back_shiny"]
        })
    

    types = []
    for tipo in data["types"]:
        types.append(tipo["type"]["name"])

    weight = data["weight"]

    linkMoves = []
    for move_actual in data["moves"]:
        linkMoves.append(move_actual["move"]["url"])
        if(len(linkMoves)>9):
            break

    movesPokemon = fetch_moves_parallel(linkMoves)
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

    data = [
        {
            "height": height,
            "id": id,
            "name": name,
            "stats": stats,
            "sprites": sprites,
            "types": types,
            "weight": weight,
            "moves": moves
        }
    ]

    return data

def validar_pokemon(data):
    if "id" not in data or "name" not in data:
        return False
    return True

def obtener_pokemon_adaptado(urls):
    data = fetch_pokemon_parallel(urls)

    if data is None:
        return None

    if not validar_pokemon(data):
        return None

    pokemon = adaptar_pokemon(data)
    return pokemon