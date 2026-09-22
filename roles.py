from data import Event, EventType

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

    def use_ability(self, target):
        target.alive = False