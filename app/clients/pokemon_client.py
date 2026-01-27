import requests
from concurrent.futures import ThreadPoolExecutor

class PokemonClient:
    def __init__(self):
        self._cache = {}
        self._cacheMoves = {}

    def fetch_pokemon_detail(self, id): #id o nombre    
        if id in self._cache:
            data = self._cache[id]
            return data
          
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        
        try:
            response = requests.get(url)
            data = response.json()
         
            self._cache[id] = data
            
            return data
        except Exception as e:
            print(f"Error desconocido: {e}")
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


def fetch_pokemon_parallel(urls, pokemon_client: PokemonClient):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(pokemon_client.fetch_pokemon_detail, urls))

def fetch_moves_parallel(urls_moves, pokemon_client: PokemonClient):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(pokemon_client.fetch_moves_detail, urls_moves))

# if __name__ == "__main__":
#     pokemons = fetch_products_parallel(urls)
#     for pokemon in pokemons:
#         print(pokemon["name"])
