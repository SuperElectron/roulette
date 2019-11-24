# roulette/roulette/bet.py


class Bet():
    """Create a new Bet of a specific amount on a specific outcome."""

    def __init__(self, amount, outcome):

        self.amount_bet = amount
        self.outcome = outcome

    def __str__(self):
        return "{} on {}".format(self.amount_bet, self.outcome)

    def __repr__(self):
        return "{} on {}".format(self.amount_bet, self.outcome)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return str(self) != str(other)

    def win_amount(self):
        """Compute the amount won, given the amount of this bet."""
        return self.amount_bet + self.outcome.winAmount(self.amount_bet)

    def get_amount(self):
        """Returns the amount bet."""
        return self.amount_bet

    def get_outcome(self):
        """Returns the outcome of the bet."""
        return self.outcome
