"""
Script which simulates a pokemon battle.
"""

import json

from pokemon.pokemon import Pokemon, moves


# List of all the current pokemon types in the game
pokemon_types = json.load(open("pokemon_types.json"))


def take_turn(p0, p1, move0_name, move1_name):
    """
    The main function that I am trying to expose.
    """
    move0 = moves[move0_name]
    move1 = moves[move1_name]

    # Use the moves
    # TODO: Choose who goes first based on speed stat
    print(f"{p0.name} used {move0}!")
    move0(p0, p1)

    print(f"{p1.name} used {move1}!")
    move1(p1, p0)


def print_scene(p0, p1):
    print(p0)
    print(p1)


def choose_moves(p0, p1):
    choice0 = int(input(f"{p0.name}'s Move? "))
    choice1 = int(input(f"{p1.name}'s Move? "))

    return pokemon0.moves[choice0],  pokemon1.moves[choice1]


if __name__ == "__main__":
    # The two pokemon battling
    pokemon0 = Pokemon(pokemon_types[0], level=5)
    pokemon1 = Pokemon(pokemon_types[1], level=5)

    # Keep battling until one pokemon faints
    while pokemon0.hp > 0 and pokemon1.hp > 0:
        print_scene(pokemon0, pokemon1)

        # Select the move
        move0_name, move1_name = choose_moves(pokemon0, pokemon1)

        take_turn(pokemon0, pokemon1, move0_name, move1_name)

        # TODO: Don't let both pokemon faint on the same turn (unless self destruct is used I guess...)
        if pokemon0.hp <= 0:
            print(f"{pokemon0.name} fainted!")
        if pokemon1.hp <= 0:
            print(f"{pokemon1.name} fainted!")
