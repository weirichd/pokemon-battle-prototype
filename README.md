# Pokemon Battle Prototype

A pokemon battle system implemented in python.

Features implemented:

- [x] Pokemon can use moves
- [ ] Teams larger than 1
- [x] Stat lowering/buffing moves
- [ ] Pokemon types
- [ ] Swapping pokemon
- [ ] Critical hits
- [ ] Status Effects
- [ ] 2 turn moves (dig, fly, hyper beam, etc.)


## Overview

This project is trying to implement pokemon battles.
The main thing I want to do is create some function 

```python
def take_turn(player1_team, player2_team, action_player, action_player2):
    # Implementation here
    return SUCCESS  # Or whatever
```

which will determine how to properly update the state of the
player's teams given the chosen actions. Actions could be
a pokemon move, swapping active pokemon, or using an item (maybe).

---

The way that players will actually build their teams is outside the scope of this
project. I might add a little utility do that at some point but most likely
it will just be read from a JSON file.

## Design Ideas

The inputs to the two 

### Teams

* Teams will be a list of 1-6 pokemon.
* One pokemon is considered "active" (the one that is out right now).
* Each turn, the player's can direct the active pokemon to use a move,
or switch active pokemon.
* If the active pokemon's HP reaches 0, then the player must select a new active
pokemon _before_ the next turn starts.


I'm thinking that teams will be a class. But maybe just a list.


### Pokemon Species

Each individual pokemon has a species.

* Base stats
* What moves the pokemon can learn
* The pokemon's type

Right now I am storing these in the file `pokemon_types.json`.
I think that I can store all the data about a species in a dictionary, 
but it might be nice to have it as a dataclass instead.

### Individual Pokemon

Each pokemon will have stats which are calculated from its species base
stats and it's level. In the actual game, there are also individual
difference between pokemon between species but I don't think I will
worry about that for now.

Pokemon can learn up to 4 moves that are possible for their species to learn.
We will need to know what moves each pokemon has learned.

These will definitely need to be a class.

### Moves

Moves are what the pokemon can do each turn.
Moves can do basically anything, so I plan on implementing them
as a callable.

Moves will also have some text that will display as the turn resolves.

Right now, I am thinking that there will be a `Move` class which all moves
are instances of.