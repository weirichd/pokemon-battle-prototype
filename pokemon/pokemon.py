"""
This module contains all the code for pokemon and moves.
"""

from typing import Callable, List


class Pokemon:
    """
    Class that represents a particular pokemon
    """

    def __init__(self, species):
        self.name: str = species["name"]
        self.moves: List[str] = species["moves"]
        self.move_names: List[str] = [moves[m].name for m in species['moves']]
        self.max_hp: int = species["stats"]["hp"]
        self.hp: int = self.max_hp
        self.attack: int = species["stats"]['attack']
        self.defense: int = species["stats"]['defence']

    def damage(self, amount):
        self.hp -= amount

    def __repr__(self):
        result = (
            f"{self.name}\n" + f"    HP: {self.hp}/{self.max_hp}\n" + "    Moves:\n"
        )
        for i, move in enumerate(self.move_names):
            result = result + f"     ({i}) {move}\n"

        return result


class Move:
    def __init__(self, name: str, use_func: Callable[[Pokemon, Pokemon], None]):
        self.name = name
        self.use_func = use_func

    def __call__(self, pokemon_user, pokemon_target):
        self.use_func(pokemon_user, pokemon_target)

    def __repr__(self):
        return self.name


class DamagingMove(Move):
    """
    A move that uses the normal damaging formula:

    Damage = max(Base Damage + User Attack - Target Defence, 0)
    """
    def __init__(self, name: str, base_damage: int):
        def do_damage(pokemon_user: Pokemon, pokemon_target: Pokemon):
            damage_amount = base_damage + pokemon_user.attack - pokemon_target.defense
            damage_amount = max(damage_amount, 0)

            pokemon_target.damage(damage_amount)

        super(DamagingMove, self).__init__(name, do_damage)


moves = {
    'thunder_shock': DamagingMove('Thunder Shock', 4),
    'scratch': DamagingMove('Scratch', 3)
}
