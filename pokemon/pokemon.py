"""
This module contains all the code for pokemon and moves.
"""

from typing import Callable, List, Dict


# This dict contains the multipliers for stats when they are raised or lowered
# Source: https://www.dragonflycave.com/mechanics/stat-stages
stat_level_multipliers: Dict[int, float] = {
    -6: 0.25,
    -5: 0.28,
    -4: 0.33,
    -3: 0.4,
    -2: 0.5,
    -1: 0.66,
    0: 1.0,
    1: 1.5,
    2: 2.0,
    3: 2.5,
    4: 3.0,
    5: 3.5,
    6: 4.0,
}


class Pokemon:
    """
    Class that represents a particular pokemon
    """

    def __init__(self, species, level: int):
        self.name: str = species["name"]
        self.level = level

        # Moves
        self.moves: List[str] = species["moves"]
        self.move_names: List[str] = [moves[m].name for m in species["moves"]]

        # Base stats for this pokemon
        self.base_hp: int = species["stats"]["hp"]
        self.base_attack: int = species["stats"]["attack"]
        self.base_defense: int = species["stats"]["defence"]

        # Current stats
        self.hp: int = self.base_hp
        self.attack: int = self.base_attack
        self.defense: int = self.base_defense

        # Current stat levels
        self.attack_level: int = 0
        self.defense_level: int = 0

    def damage(self, amount):
        """Lower the pokemon's HP by amount"""
        self.hp -= amount
        self.hp = max(self.hp, 0)

    def change_stat_level(self, attack_level_change=0, defence_level_change=0):
        """Apply a stat level change. Return False if nothing happened."""
        self.attack_level += attack_level_change
        self.defense_level += defence_level_change

        self.attack_level = max(min(self.attack_level, 6), -6)
        self.defense_level = max(min(self.defense_level, 6), -6)

        # Recalculate stats
        self.attack = int(self.base_attack * stat_level_multipliers[self.attack_level])
        self.defense = int(self.base_defense * stat_level_multipliers[self.defense_level])

    def __repr__(self):
        result = (
            f"{self.name} (LVL {self.level})\n"
            + f"    HP: {self.hp}/{self.base_hp}\n"
            + "    Moves:\n"
        )
        for i, move in enumerate(self.move_names):
            result = result + f"     ({i}) {move}\n"

        return result


class Move:
    """
    Base class for all moves.
    """
    def __init__(self, name: str, use_func: Callable[[Pokemon, Pokemon], None]):
        self.name = name
        self.use_func = use_func

    def __call__(self, pokemon_user, pokemon_target):
        self.use_func(pokemon_user, pokemon_target)

    def __repr__(self):
        return self.name


# Some classes for a few common move types.


class DamagingMove(Move):
    """
    A move that uses the normal damaging formula:

    # TODO: Use the real damage formula.
    Source for damage formula: https://bulbapedia.bulbagarden.net/wiki/Damage
    """

    def __init__(self, name: str, base_damage: int):
        def do_damage(pokemon_user: Pokemon, pokemon_target: Pokemon):
            damage_amount = base_damage + pokemon_user.attack - pokemon_target.defense
            damage_amount = max(damage_amount, 0)

            pokemon_target.damage(damage_amount)

            print(f"It did {damage_amount} damage!")

        super(DamagingMove, self).__init__(name, do_damage)


class OpponentStatAlterMove(Move):
    """
    A move that alters the opposing pokemon's stats.
    """

    def __init__(
        self,
        name: str,
        state_to_change: str,
        attack_level_change: int = 0,
        defence_level_change: int = 0,
    ):
        def update_stat(_: Pokemon, pokemon_target: Pokemon):
            pokemon_target.change_stat_level(
                attack_level_change=attack_level_change,
                defence_level_change=defence_level_change,
            )

            # TODO: Try to think of a better way to do this, potentially.
            # TODO: Also, when altering stats by two levels it should say "sharply fell"
            # TODO: Also, it should print a different message when the level can't drop any more
            #       "Nothing happened."
            print(f"{pokemon_target.name}'s {state_to_change} fell!")

        super(OpponentStatAlterMove, self).__init__(name, update_stat)


# TODO: Eventually move this out to another module

moves = {
    "thunder_shock": DamagingMove("Thunder Shock", 4),
    "scratch": DamagingMove("Scratch", 3),
    "growl": OpponentStatAlterMove("Growl", 'attack', attack_level_change=-1),
    "tail_wag": OpponentStatAlterMove("Tail Wag", 'defence', defence_level_change=-1),
}
