import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://pokeapi.co/api/v2/pokemon/1",
    "https://pokeapi.co/api/v2/pokemon/2",
    "https://pokeapi.co/api/v2/pokemon/3",
    "https://pokeapi.co/api/v2/pokemon/4",
    "https://pokeapi.co/api/v2/pokemon/5"
]

def fetch_pokemon_list(lista):
    response = requests.get(lista)
    return response.json()

def fetch_pokemon_detail(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None

def fetch_products_parallel(urls):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(fetch_pokemon_detail, urls))
    

# if __name__ == "__main__":
#     pokemons = fetch_products_parallel(urls)
#     for pokemon in pokemons:
#         print(pokemon["name"])