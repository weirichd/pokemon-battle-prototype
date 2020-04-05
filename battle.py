"""
Script which simulates a pokemon battle.
"""

import json

from pokemon.pokemon import Pokemon, moves


# List of all the current pokemon types in the game
pokemon_types = json.load(open("pokemon_types.json"))


def print_scene(p0, p1):
    print(pokemon0)
    print(pokemon1)


if __name__ == "__main__":
    # The two pokemon battling
    pokemon0 = Pokemon(pokemon_types[0], level=5)
    pokemon1 = Pokemon(pokemon_types[1], level=5)

    # Keep battling until one pokemon faints
    while pokemon0.hp > 0 and pokemon1.hp > 0:
        print_scene(pokemon0, pokemon1)

        # Select the move
        choice0 = int(input(f"{pokemon0.name}'s Move? "))
        choice1 = int(input(f"{pokemon1.name}'s Move? "))

        move0 = moves[pokemon0.moves[choice0]]
        move1 = moves[pokemon1.moves[choice1]]

        # Use the moves
        # TODO: Choose who goes first based on speed stat
        print(f"{pokemon0.name} used {move0}!")
        move0(pokemon0, pokemon1)

        print(f"{pokemon1.name} used {move1}!")
        move1(pokemon1, pokemon0)

        # TODO: Don't let both pokemon faint on the same turn (unless self destruct is used I guess...)
        if pokemon0.hp <= 0:
            print(f"{pokemon0.name} fainted!")
        if pokemon1.hp <= 0:
            print(f"{pokemon1.name} fainted!")
