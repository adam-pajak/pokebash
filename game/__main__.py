from game.battle import Battle
from game.pokedex import choose_pokemon
from game.pokemon import HumanTrainer, ComputerTrainer

def main():
    battle = Battle(
        player=HumanTrainer(choose_pokemon("Choose your Pokemon")),
        computer=ComputerTrainer(choose_pokemon("Choose opponent's Pokemon"))
    )
    battle.show_stats()
    battle.play()