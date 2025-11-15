import random

from app.services.pokemon_service import listar_pokemon
from app.models.battle import Battle

# Para no tener que ir cambiando las variables 1 a 1 cuando toquemos el daño
MULTIPLICADOR_DAÑO = 0.20


def random_moves(pokemon):
    movimientos = random.sample(pokemon.moves, min(4, len(pokemon.moves)))

    return movimientos


def random_pokemon():
    lista_pokemons = listar_pokemon()

    pokemon = random.choice(lista_pokemons)

    return pokemon


def random_atacar(ataques):
    return random.choice(ataques)


# para poder conseguir el atributo hp en el json data
def get_stat_value(pokemon, stat_name):
    for stat in pokemon.stats:
        if stat["name"] == stat_name:
            return stat["value"]


def atacar_jugador(damage, accuracy, battle_object, pokemon_name, ataque_name) -> bool:
    # Serperior tiene un ataque con accuracy null
    if not accuracy:
        accuracy = 100

    acierta = random.randint(1, 100) <= accuracy
    nombre_rival = battle_object["datos_pokemon_rival"].name.capitalize(
    )

    acabar_batalla = False

    if acierta:
        battle_object["vida_rival"] = round(
            battle_object["vida_rival"] - (damage * MULTIPLICADOR_DAÑO), 2)

        if battle_object["vida_rival"] <= 0:
            battle_object["log"].append(
                f"{pokemon_name.capitalize()} utilizó {ataque_name.upper()}. {nombre_rival.capitalize()} pierde {damage*MULTIPLICADOR_DAÑO} puntos de salud. PS restantes: 0")

            battle_object["log"].append(
                f"{nombre_rival.capitalize()} se ha debilitado. HAS GANADO")

            acabar_batalla = True

            return acabar_batalla, battle_object
        else:
            battle_object["log"].append(
                f"{pokemon_name.capitalize()} utilizó {ataque_name.upper()}. {nombre_rival.capitalize()} pierde {damage*MULTIPLICADOR_DAÑO} puntos de salud. PS restantes: {battle_object['vida_rival']}")
    else:
        battle_object["log"].append(
            f"{pokemon_name.capitalize()} falla su ataque...")

    return acabar_batalla, battle_object


def atacar_rival(damage, accuracy, battle_object, pokemon_name, ataque_name) -> bool:
    # Serperior tiene un ataque con accuracy null
    if not accuracy:
        accuracy = 100

    acierta = random.randint(1, 100) <= accuracy
    nombre_rival = battle_object["datos_pokemon_rival"].name.capitalize(
    )

    acabar_batalla = False

    if acierta:
        battle_object["vida_jugador"] = round(
            battle_object["vida_jugador"] - (damage*MULTIPLICADOR_DAÑO), 2)

        if battle_object["vida_jugador"] <= 0:
            battle_object["log"].append(
                f"{pokemon_name.capitalize()} se ha debilitado. HAS PERDIDO")

            acabar_batalla = True

            return acabar_batalla, battle_object

        battle_object["log"].append(
            f"{nombre_rival.capitalize()} utilizó {ataque_name.upper()}. {pokemon_name.capitalize()} pierde {damage*MULTIPLICADOR_DAÑO} puntos de salud. PS restantes: {battle_object['vida_jugador']}")
    else:
        battle_object["log"].append(
            f"{nombre_rival.capitalize()} falla su ataque...")

    return acabar_batalla, battle_object


def inicializar_batalla(pokemon_elegido):
    pokemon_rival = random_pokemon()
    moves_elegido = random_moves(pokemon_elegido)
    moves_rival = random_moves(pokemon_rival)

    battle = Battle(
        datos_pokemon_jugador=pokemon_elegido,
        datos_pokemon_rival=pokemon_rival,
        vida_jugador=get_stat_value(pokemon_elegido, "hp"),
        vida_rival=get_stat_value(pokemon_rival, "hp"),
        ataques_jugador=moves_elegido,
        ataques_rival=moves_rival
    )

    return battle
