import json
import pathlib
from copy import deepcopy
from typing import List

from game.pokemon import Pokemon, Move, LEVEL

POKEDEX = []

def choose_pokemon(message: str) -> Pokemon:
    for pokemon in load():
        print(f"- {pokemon.name}")
    print(message)
    while True:
        name = input("Input Pokémon name from the list above: ")
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
                    attack=compute_stat_for_level('attack', int(element['attack']), LEVEL),
                    defense=compute_stat_for_level('defense',  int(element['defense']), LEVEL),
                    speed=compute_stat_for_level('speed', int(element['speed']), LEVEL),
                    health=compute_stat_for_level('hp', int(element['hp']), LEVEL),
                    moves=moves,
            ))

    return POKEDEX

def compute_stat_for_level(kind: str, value: int, level: int) -> int:
    # formula: https://bulbapedia.bulbagarden.net/wiki/Stat#Base_stat_values
    if level == 100:
        if kind == "hp":
            return value * 2 + 110
        return value * 2 + 5
    return value