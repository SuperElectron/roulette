# roulette/roulette/outcome.py


import hashlib


class Outcome(object):
    """Provide winning amount for a specific bet.

    Stores name and odds of a specific bet in roulette and
    calculates winning amount for a specific bet amount on that
    outcome.

    Attributes:
        name: A string indicating the name of the bet.
        payout: The payout of the bet, i.e. the multiplyer for the bet amount.
    """

    def winAmount(self, amount):
        """Returns winning amount for a bet amount placed."""
        return self.odds * amount

    def getName(self):
        """Returns string name of the table-bet."""
        return self.name

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{} ({}:1)".format(self.name, self.odds)

    def __repr__(self):
        return "{} ({}:1)".format(self.name, self.odds)

    def __hash__(self):
        return int(hashlib.md5(self.name.encode('utf-8')).hexdigest(), 16)
