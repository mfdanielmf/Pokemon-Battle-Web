import time
import requests
from concurrent.futures import ThreadPoolExecutor

TIEMPO_LIMITE = 300  # 5 min máximo para el cache


class PokemonClient:
    def __init__(self):
        self._cache = {}
        self._cacheMoves = {}

    def fetch_pokemon_detail(self, id):  # id o nombre
        if id in self._cache:
            data = self._cache[id]

            # Si pasó el tiempo límite, devolvemo data, si no hace el req
            if time.time() - data["expiracion"] < TIEMPO_LIMITE:
                return data

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"

        try:
            response = requests.get(url)
            data = response.json()
            data["expiracion"] = time.time()

            self._cache[id] = data

            return data
        except Exception as e:
            print(f"Error desconocido: {str(e)}")
            return None

    def fetch_moves_detail(self, url):
        if url in self._cacheMoves:
            data = self._cacheMoves[url]
            return data

        try:
            response = requests.get(url)
            data = response.json()
            self._cacheMoves[url] = data
            return data
        except Exception as e:
            print(f"Error desconocido: {e}")
            return None

    def fetch_pokemon_random(self):
        url = f"https://pokeapi.co/api/v2/pokemon?limit=10000"

        try:
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            print(f"Error desconocido: {e}")
            return None

    def fetch_pokemon_list(self, limit, offset):
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"

        try:
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            print(f"Error desconocido: {e}")
            return None


def fetch_pokemon_parallel(urls, pokemon_client: PokemonClient):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(pokemon_client.fetch_pokemon_detail, urls))


def fetch_moves_parallel(urls_moves, pokemon_client: PokemonClient):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(pokemon_client.fetch_moves_detail, urls_moves))
