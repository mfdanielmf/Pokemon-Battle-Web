from app.services.battle_service import random_pokemon, get_stat_value
from unittest.mock import patch

def test_random_pokemon():
    with patch("app.services.pokemon_service.listar_pokemon") as mock_pokemon:
        mock_pokemon.return_value = ["Pikachu", "Dani", "Fran"]
        with patch("app.services.battle_service.random.choice") as mock_random:
            
            mock_random.return_value = "Pikachu"
            resultado = random_pokemon()
            print(resultado)
            assert resultado == "Pikachu"

# def test_get_stat_value():
#     resultado = get_stat_value("Pikachu","hp")
    