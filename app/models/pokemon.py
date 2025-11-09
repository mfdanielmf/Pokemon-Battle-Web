class Pokemon:
    def __init__(self, height, id, name, weight, stats, sprites, moves, types):
        self.height = height
        self.id = id
        self.name = name
        self.weight = weight
        self.stats = stats
        self.sprites = sprites
        self.moves = moves
        self.types = types

    def to_dict(self):
        return {
            "height": self.height,
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "stats": self.stats,
            "sprites": self.sprites,
            "moves": self.moves,
            "types": self.types
        }

    def __str__(self):
        return f"{self.name.capitalize()} ID: {self.id}"
