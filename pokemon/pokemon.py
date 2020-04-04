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


moves = {
    'thunder_shock': Move('Thunder Shock', lambda _, p2: p2.damage(4)),
    'scratch': Move('Scratch', lambda _, p2: p2.damage(3))
}
