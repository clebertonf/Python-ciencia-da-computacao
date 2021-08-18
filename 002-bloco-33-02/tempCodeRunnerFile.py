import json



with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

grass_type_pokemons = filter(lambda poke: poke['type'] == 'Grass', pokemons)

for poke in grass_type_pokemons:
    print(poke)
