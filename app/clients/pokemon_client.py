import requests
from concurrent.futures import ThreadPoolExecutor


def fetch_pokemon_detail(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None


def fetch_pokemon_parallel(urls):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(fetch_pokemon_detail, urls))


def fetch_moves_detail(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None


def fetch_moves_parallel(urls_moves):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(fetch_moves_detail, urls_moves))

# if __name__ == "__main__":
#     pokemons = fetch_products_parallel(urls)
#     for pokemon in pokemons:
#         print(pokemon["name"])
