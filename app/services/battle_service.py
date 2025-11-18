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


def atacar(damage, accuracy, battle_object, pokemon_name, ataque_name, atacante_jugador) -> bool:
    # Serperior tiene un ataque con accuracy null
    if not accuracy:
            accuracy = 100

    acierta = random.randint(1, 100) <= accuracy
    nombre_rival = battle_object["datos_pokemon_rival"].name.capitalize(
    )

    acabar_batalla = False

    nombre_pokemon_rival = battle_object["datos_pokemon_rival"].name

    if atacante_jugador:
        nombre_pokemon_atacante = pokemon_name
        nombre_pokemon_defensor = nombre_pokemon_rival
        vida_pokemon_rival = "vida_rival"   #para bajarle la vida al pokemon rival
        #es para hacer  battle_object["vida_rival"] o battle_object["vida_jugador"]

    if atacante_jugador == False:
        nombre_pokemon_atacante = nombre_pokemon_rival
        nombre_pokemon_defensor = pokemon_name
        vida_pokemon_rival = "vida_jugador" 
        
    if acierta:
        battle_object[vida_pokemon_rival] = round(
            battle_object[vida_pokemon_rival] - (damage * MULTIPLICADOR_DAÑO), 2)

        if battle_object[vida_pokemon_rival] <= 0:
            battle_object["log"].append(
                f"{nombre_pokemon_atacante.capitalize()} utilizó {ataque_name.upper()}. {nombre_pokemon_defensor.capitalize()} pierde {damage*MULTIPLICADOR_DAÑO} puntos de salud. PS restantes: 0")

            battle_object["log"].append(
                f"{nombre_pokemon_defensor.capitalize()} se ha debilitado. HAS GANADO")

            acabar_batalla = True

            return acabar_batalla, battle_object

        battle_object["log"].append(
            f"{nombre_pokemon_defensor.capitalize()} utilizó {ataque_name.upper()}. {nombre_pokemon_defensor.capitalize()} pierde {damage*MULTIPLICADOR_DAÑO} puntos de salud. PS restantes: {battle_object[vida_pokemon_rival]}")
    else:
        battle_object["log"].append(
            f"{nombre_pokemon_defensor.capitalize()} falla su ataque...")

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
