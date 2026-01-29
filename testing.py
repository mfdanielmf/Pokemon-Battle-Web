import requests

URL = "https://pokeapi.co/api/v2/pokemon/1/"


def obtener_data(url):
    req = requests.get(url)

    if req.status_code == 200:
        return req.json()

    raise Exception()


"""
VAMOS A GUARDAR ALGO ASÍ

pokemons = [
    {
        "id": 1,                                    -> data["id"]
        "nombre": "charizard",                      -> data["name"]
        "vida": 1323232323223,                      -> data["stats"] for stat in stats   stat["base_stat"](esto de aqui es el valor) stat["stat"] stat["name"] == hp
        "peso": 32,                                 -> data["weight"]
        "tipos": ["fuego", "lo q sea"],             ->  for tipo in data["types"]: tipo["type"]["name"]
        "ataques": [
            {
                "nombre": "lo q sea",
                "daño": 32,
                "precision": 100
            }
        ]
    },
    {
        "id": 2,
        "nombre": "pikachu",
        "vida": 132,
        "peso": 32,
        "tipos": ["electrico", "lo q sea"],
        "ataques": [
            {
                "nombre": "lo q sea",
                "daño": 32,
                "precision": 100
            }
        ]
    },
]




"""


if __name__ == "__main__":
    try:
        data = obtener_data(URL)

        # for stat_actual in data["stats"]:

        #     nombre_stat = stat_actual["stat"]["name"]
        #     if nombre_stat == "hp":
        #         print(stat_actual["base_stat"])

        for tipo in data["types"]:
            print(tipo["type"]["name"])

    except Exception:
        pass
