import random

from flask import session
from app.services.pokemon_service import listar_pokemon
from app.services.current_year_service import get_current_year

current_year = get_current_year()


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


def atacar_jugador(damage, accuracy, battle_object, pokemon_name, ataque_name):
    # Serperior tiene un ataque con accuracy null
    if not accuracy:
        accuracy = 100

    acierta = random.randint(1, 100) <= accuracy
    nombre_rival = battle_object["datos_pokemon_rival"].name.capitalize(
    )

    acabar_batalla = False

    if acierta:
        battle_object["vida_rival"] = round(
            battle_object["vida_rival"] - (damage * 0.20), 2)

        battle_object["log"].append(
            f"{pokemon_name.capitalize()} utilizó {ataque_name.upper()}. {nombre_rival.capitalize()} pierde {damage*0.20} puntos de salud. PS restantes: {battle_object['vida_rival']}")

        if battle_object["vida_rival"] <= 0:
            battle_object["log"].append(
                f"{nombre_rival.capitalize()} se ha debilitado")

            acabar_batalla = True

            return acabar_batalla
    else:
        battle_object["log"].append(
            f"{pokemon_name.capitalize()} falla su ataque...")

    session["battle"] = battle_object

    return acabar_batalla


def atacar_rival(damage, accuracy, battle_object, pokemon_name, ataque_name):
    # Serperior tiene un ataque con accuracy null
    if not accuracy:
        accuracy = 100

    acierta = random.randint(1, 100) <= accuracy
    nombre_rival = battle_object["datos_pokemon_rival"].name.capitalize(
    )

    acabar_batalla = False

    if acierta:
        battle_object["vida_jugador"] = round(
            battle_object["vida_jugador"] - (damage*0.20), 2)

        if battle_object["vida_jugador"] <= 0:
            battle_object["log"].append(
                f"{pokemon_name.capitalize()} se ha debilitado")

            acabar_batalla = True

            return acabar_batalla

        battle_object["log"].append(
            f"{nombre_rival.capitalize()} utilizó {ataque_name.upper()}. {pokemon_name.capitalize()} pierde {damage*0.20} puntos de salud. PS restantes: {battle_object['vida_jugador']}")
    else:
        battle_object["log"].append(
            f"{nombre_rival.capitalize()} falla su ataque...")

    session["battle"] = battle_object

    return acabar_batalla
