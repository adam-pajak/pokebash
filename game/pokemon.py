import random
from typing import List


LEVEL = 100

TYPES = [
    'normal', 'fighting', 'flying', 'poison', 'ground', 'rock',
    'bug', 'ghost', 'fire', 'water', 'grass', 'electric',
    'psychic', 'ice', 'dragon'
]

EFFECTIVENESS = {
    'normal':  {'rock': 0.5, 'ghost': 0.0},
    'fighting': {'normal': 2.0, 'rock': 2.0, 'ice': 2.0, 'ghost': 0.0, 'flying': 0.5, 'poison': 0.5, 'psychic': 0.5, 'bug': 0.5},
    'flying': {'fighting': 2.0, 'bug': 2.0, 'grass': 2.0, 'rock': 0.5, 'electric': 0.5},
    'poison': {'grass': 2.0, 'fairy': 2.0, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'ghost': 0.5},
    'ground': {'poison': 2.0, 'rock': 2.0, 'fire': 2.0, 'electric': 2.0, 'bug': 0.5, 'grass': 0.5, 'flying': 0.0},
    'rock': {'fire': 2.0, 'ice': 2.0, 'flying': 2.0, 'bug': 2.0, 'fighting': 0.5, 'ground': 0.5},
    'bug': {'grass': 2.0, 'psychic': 2.0, 'dark': 2.0, 'fire': 0.5, 'fighting': 0.5, 'poison': 0.5, 'flying': 0.5, 'ghost': 0.5},
    'ghost': {'ghost': 2.0, 'psychic': 2.0, 'normal': 0.0},
    'fire': {'grass': 2.0, 'ice': 2.0, 'bug': 2.0, 'fire': 0.5, 'water': 0.5, 'rock': 0.5, 'dragon': 0.5},
    'water': {'fire': 2.0, 'ground': 2.0, 'rock': 2.0, 'water': 0.5, 'grass': 0.5, 'dragon': 0.5},
    'grass': {'water': 2.0, 'ground': 2.0, 'rock': 2.0, 'flying': 0.5, 'poison': 0.5, 'bug': 0.5, 'fire': 0.5, 'grass': 0.5, 'dragon': 0.5},
    'electric': {'water': 2.0, 'flying': 2.0, 'electric': 0.5, 'grass': 0.5, 'dragon': 0.5, 'ground': 0.0},
    'psychic': {'fighting': 2.0, 'poison': 2.0, 'psychic': 0.5},
    'ice': {'grass': 2.0, 'ground': 2.0, 'flying': 2.0, 'dragon': 2.0, 'fire': 0.5, 'water': 0.5, 'ice': 0.5},
    'dragon': {'dragon': 2.0}
}
def calculate_effectiveness(
    attack_type: str,
    defend_types:List[str]
) -> float:
    attack = attack_type.lower()
    total = 1.0
    for target in defend_types:
        total *= EFFECTIVENESS[attack].get(target.lower(), 1.0)
    return total

class Move:
    def __init__(self, name: str, power: int, accuracy: int , type: str):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type

class Pokemon:
    def __init__(self, name: str, types: List[str], moves: List[Move], attack: int, defense: int, health: int, speed: int):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.health = health
        self.speed = speed


class Trainer:
    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
    def choose_move(self) -> Move:
        raise NotImplementedError


class ComputerTrainer(Trainer):
    def choose_move(self) -> Move:
        return random.choice(self.pokemon.moves)

class HumanTrainer(Trainer):
    def choose_move(self) -> Move:
        while True:
            print("Choose move: ")
            for idx, move in enumerate(self.pokemon.moves):
                print(f"{idx + 1}) {move.name}")
            try:
                return self.pokemon.moves[int(input("> "))-1]
            except:
                print("Invalid number.")


def move_hits(accuracy: int) -> bool:
    return random.randint(1, 100) <= accuracy


def calculate_damage(
        attacker: Pokemon,
        defender: Pokemon,
        strike: Move
) -> int:
    # Formula: https://bulbapedia.bulbagarden.net/wiki/Damage#Example
    stab = 1.0
    if strike.type in attacker.types:
        stab = 1.5
    if attacker.attack > 255 or defender.defense > 255:
        attacker.attack /= 4
        attacker.attack = int(attacker.attack)
        defender.defense /= 4
        defender.defense = int(defender.defense)
    damage = stab * ((((2 * LEVEL / 5 + 2) * strike.power * (attacker.attack / defender.defense)) / 50) + 2) * calculate_effectiveness(strike.type, defender.types)
    if damage > 1.0:
        random_factor = (217.0 + 38.0 * random.random()) / 255.0
        damage *= random_factor
    return int(damage)