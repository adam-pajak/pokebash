import time
from game.console import green, red, delay_print
from game.pokemon import Pokemon, Trainer, calculate_damage, Move, calculate_effectiveness, move_hits


def show_pokemon_stats(pokemon: Pokemon):
    print(pokemon.name)
    print(f"Types: {pokemon.types}")
    print("Moves: ")
    for move in pokemon.moves:
        print(f"- {move.name}, power: {move.power}, type: {move.type}")
    print(f"Level: 100, Attack: {pokemon.attack}, Defense: {pokemon.defense}, Speed: {pokemon.speed}, Health: {pokemon.health}")


def attack(attacker: Pokemon, defender: Pokemon, move: Move) -> bool:
    delay_print(f"{attacker.name} used {move.name}!")
    if move_hits(move.accuracy):
        damage = calculate_damage(attacker, defender, move)
        if calculate_effectiveness(move.type, defender.types) > 1.0:
            delay_print("It's super effective!")
        elif calculate_effectiveness(move.type, defender.types) < 1.0:
            delay_print("It's not very effective!")
        delay_print(f"{move.name} caused {damage} damage to {defender.name}")
        defender.health -= damage
    else:
        delay_print(f"{defender.name} avoided the attack!")
    return defender.health > 0


class Battle:
    def __init__(self, player: Trainer, computer: Trainer):
        self.player = player
        self.computer = computer
        self.first, self.second = self.player, self.computer
        if self.player.pokemon.speed < self.computer.pokemon.speed:
            self.first, self.second = self.computer, self.player

    def show_stats(self):
        print("Your Pokemon Stats:")
        show_pokemon_stats(self.player.pokemon)
        time.sleep(1.5)
        print("Opponent Pokemon Stats:")
        show_pokemon_stats(self.computer.pokemon)

        time.sleep(3)
        delay_print("\nYour rival wants to battle!")
        delay_print(f"Rival sent out {self.computer.pokemon.name}!")
        delay_print(f"Go! {self.player.pokemon.name}!")

    def play(self):
        while self.play_round():
            pass
        if self.player.pokemon.health > 0:
            delay_print(f"{self.computer.pokemon.name} fainted!")
            green("You defeated your rival!")
        else:
            delay_print(f"{self.player.pokemon.name} fainted!")
            red("You lost to your rival!")

    def play_round(self) -> bool:
        green(f"{self.player.pokemon.name} ♥ {self.player.pokemon.health}")
        green(f"{self.computer.pokemon.name} ♥ {self.computer.pokemon.health}")

        first_move = self.first.choose_move()
        second_move = self.second.choose_move()
        if not attack(self.first.pokemon, self.second.pokemon, first_move):
            return False
        return attack(self.second.pokemon, self.first.pokemon, second_move)