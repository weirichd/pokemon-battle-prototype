"""
Script which simulates a pokemon battle.
"""

# List of all the current pokemon types in the game
pokemon = [
    {
        'name': 'Charmander',
        'hp': 30,
        'moves': ['Tackle'],
    },
    {
        'name': 'Pikachu',
        'hp': 25,
        'moves': ['Thunder Shock'],
    },
]

# The damage that each move does
moves = {
    'Tackle': 3,
    'Thunder Shock': 4,
}


def output_pokemon(p):
    print(p['species']['name'])
    print(f"    HP: {p['current hp']}/{p['species']['hp']}")

    print('    Moves:')
    for i, move in enumerate(p['species']['moves']):
        print(f'     ({i}) {move}')


if __name__ == '__main__':
    # The two pokemon battling
    pokemon0 = {
        'species': pokemon[0],
        'current hp': pokemon[0]['hp'],
    }

    pokemon1 = {
        'species': pokemon[1],
        'current hp': pokemon[1]['hp'],
    }

    # Keep battling until one pokemon faints
    while pokemon0['current hp'] > 0 and pokemon1['current hp'] > 0:
        output_pokemon(pokemon0)
        output_pokemon(pokemon1)

        # Select the move
        move0 = int(input(f"{pokemon0['species']['name']}'s Move? (0-3): "))
        move1 = int(input(f"{pokemon1['species']['name']}'s Move? (0-3): "))

        print(f"{pokemon0['species']['name']} used {pokemon0['species']['moves'][move0]}!")
        print(f"{pokemon1['species']['name']} used {pokemon1['species']['moves'][move1]}!")

        # Do damage
        pokemon1['current hp'] -= moves[pokemon0['species']['moves'][move0]]
        pokemon0['current hp'] -= moves[pokemon1['species']['moves'][move1]]

        if pokemon0['current hp'] <= 0:
            print(f"{pokemon0['species']['name']} fainted!")
        if pokemon1['current hp'] <= 0:
            print(f"{pokemon1['species']['name']} fainted!")
