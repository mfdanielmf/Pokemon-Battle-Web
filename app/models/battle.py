class Battle:
    def __init__(self, datos_pokemon_jugador, datos_pokemon_rival, vida_jugador, vida_rival, ataques_jugador, ataques_rival):
        self.turno = 1
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival
        self.log = []
        self.vida_jugador = vida_jugador
        self.vida_rival = vida_rival
        self.ataques_jugador = ataques_jugador
        self.ataques_rival = ataques_rival
