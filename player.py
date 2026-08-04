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