class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        for item in self.pokemon:
            if pokemon.name == item.name:
                return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"


    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            result += f"- {pokemon.pokemon_details()}\n"
        return result

