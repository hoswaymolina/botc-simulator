import random

class Player:
    """Class for a player."""

    def __init__(self, number, role):
        self.number = number
        self.name = f"Player {number}"
        self.role = role
        self.alive = True
        self.drunk = False
        self.poisoned = False
        self.nomination_left = True

    def __repr__(self):
        status = "alive" if self.alive else "dead"
        return (f"{self.name} ({self.role}, {self.role.alignment}, {status})")


class Role:
    """Base class for all roles."""

    def __repr__(self):
        return self.__class__.__name__

class Townsfolk(Role):
    alignment = 'good'

class Outsider(Role):
    alignment = 'good'

class Minion(Role):
    alignment = 'evil'

class Demon(Role):
    alignment = 'evil'


class Washerwoman(Townsfolk):
    """Class representing the Washerwoman role."""
    pass


class Librarian(Townsfolk):
    """Class representing the Librarian role."""
    pass


class Investigator(Townsfolk):
    """Class representing the Investigator role."""
    pass


class Chef(Townsfolk):
    """Class representing the Chef role."""
    pass


class Empath(Townsfolk):
    """Class representing the Empath role."""
    pass


class FortuneTeller(Townsfolk):
    """Class representing the FortuneTeller role."""
    pass


class Undertaker(Townsfolk):
    """Class representing the Undertaker role."""
    pass


class Monk(Townsfolk):
    """Class representing the Monk role."""
    pass


class Ravenkeeper(Townsfolk):
    """Class representing the Ravenkeeper role."""
    pass


class Virgin(Townsfolk):
    """Class representing the Virgin role."""
    pass


class Slayer(Townsfolk):
    """Class representing the Slayer role."""
    pass


class Soldier(Townsfolk):
    """Class representing the Soldier role."""
    pass


class Mayor(Townsfolk):
    """Class representing the Mayor role."""
    pass


class Butler(Outsider):
    """Class representing the Butler role."""
    pass


class Saint(Outsider):
    """Class representing the Saint role."""
    pass


class Recluse(Outsider):
    """Class representing the Recluse role."""
    pass


class Drunk(Outsider):
    """Class representing the Drunk role."""
    pass


class Poisoner(Minion):
    """Class representing the Poisoner role."""
    pass


class Spy(Minion):
    """Class representing the Spy role."""
    pass


class Baron(Minion):
    """Class representing the Baron role."""
    pass


class ScarletWoman(Minion):
    """Class representing the Scarlet Woman role."""
    pass


class Imp(Demon):
    """Class representing the Imp role."""
    pass


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

    for i in range(num_townsfolk):
        roles.append(townsfolk.pop())

    for i in range(num_demons):
        roles.append(demons.pop())

    random.shuffle(roles)

    for i in range(num_players):
        players.append(Player(i+1, roles.pop()()))

    return players

players = assign_roles()

for player in players:
    print(player)