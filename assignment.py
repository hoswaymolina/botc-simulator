import random

from roles import *
from player import *

townsfolk_roles = [
    Washerwoman,
    Librarian,
    Investigator,
    Chef,
    Empath,
    FortuneTeller,
    Undertaker,
    Monk,
    Ravenkeeper,
    Virgin,
    Slayer,
    Soldier,
    Mayor
]

outsider_roles = [
    Butler,
    Saint,
    Recluse,
    Drunk
]

minion_roles = [
    Poisoner,
    Spy,
    Baron,
    ScarletWoman
]

demon_roles = [
    Imp
]

character_counts = {
    5: [3, 0, 1, 1],
    6: [3, 1, 1, 1],
    7: [5, 0, 1, 1],
    8: [5, 1, 1, 1],
    9: [5, 2, 1, 1],
    10: [7, 0, 2, 1],
    11: [7, 1, 2, 1],
    12: [7, 2, 2, 1],
    13: [9, 0, 3, 1],
    14: [9, 1, 3, 1],
    15: [9, 2, 3, 1]
}

def assign_roles(num_players=10):
    roles = []
    players = []
    num_townsfolk = character_counts[num_players][0]
    num_outsiders = character_counts[num_players][1]
    num_minions = character_counts[num_players][2]
    num_demons = character_counts[num_players][3]

    # Shuffle the roles.
    minions = minion_roles[:]
    random.shuffle(minions)

    townsfolk = townsfolk_roles[:]
    random.shuffle(townsfolk)

    outsiders = outsider_roles[:]
    random.shuffle(outsiders)

    demons = demon_roles[:]
    random.shuffle(demons)

    # Pick the minions first, to see if a Baron will affect the numbers.
    for i in range(num_minions):
        roles.append(minions.pop())

    if Baron in roles:
        num_outsiders += 2
        num_townsfolk -= 2

    for i in range(num_outsiders):
        roles.append(outsiders.pop())

    # The instructions note that before placing character tokens in the bag,
    # the drunk token is replaced with a townsfolk role (and marked as drunk).
    # In order to keep track that this particular townsfolk is drunk, and
    # because we do not know which player will get this role yet, the drunk
    # townsfolk role is stored in a "drunk_townsfolk" variable and introduced
    # during player assignment.

    if Drunk in roles:
        drunk_townsfolk = townsfolk.pop()

    for i in range(num_townsfolk):
        roles.append(townsfolk.pop())

    for i in range(num_demons):
        roles.append(demons.pop())

    random.shuffle(roles)

    for i in range(num_players):
        players.append(Player(i+1, roles.pop()()))

    for player in players:
        if isinstance(player.role, Drunk):
                player.role = drunk_townsfolk()
                player.drunk = True

    return players

players = assign_roles()

for player in players:
    print(player)
    if player.drunk:
        print("This player is drunk!")