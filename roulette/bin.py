# roulette/roulette/bin.py


class Bin(object):
    """Represents a bin of the roulette.

    Provides a frozenset of all the outcomes of placing a bet in a
    roulette bin.

    Attributes:
        outcomes: Contains all the outcomes of the bin.
    """

    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        """Adds an outcome to the bin."""
        self.outcomes |= set([outcome])

    def __contains__(self, outcome):
        return outcome in self.outcomes

    def __len__(self):
        return len(self.outcomes)

    def __str__(self):
        return ", ".join(map(str, self.outcomes))

    def __repr__(self):
        return ", ".join(map(str, self.outcomes))

