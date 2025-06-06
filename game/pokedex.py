import json
import pathlib
from copy import deepcopy
from typing import List

from game.pokemon import Pokemon, Move

POKEDEX = []

def choose_pokemon(message: str) -> Pokemon:
    print(message)
    for pokemon in load():
        print(f"- {pokemon.name}")
    while True:
        name = input("Input Pokémon name: ")
        for pokemon in load():
            if pokemon.name.lower() == name.lower():
                return deepcopy(pokemon)

        print("Invalid Pokémon name")

def load() -> List[Pokemon]:
    if len(POKEDEX) == 0:
        with open(pathlib.Path().resolve().joinpath('resources/pokedex.json'), 'r', encoding='utf-8') as f:
            data = json.load(f)

        for element in data:
            moves = []
            for move in element['moves']:
                moves.append(
                    Move(
                        name=move['name'].capitalize(),
                        type=move['type'].capitalize(),
                        power=int(move['power']),
                        accuracy=int(move['accuracy'] if move['accuracy'] else 100),
                    )
                )
            POKEDEX.append(
                Pokemon(
                    name=element['name'],
                    types=element['type'],
                    attack=int(element['attack']),
                    defense=int(element['defense']),
                    speed=int(element['speed']),
                    health=int(element['hp']),
                    moves=moves,
            ))

    return POKEDEX