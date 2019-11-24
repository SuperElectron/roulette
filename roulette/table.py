# roulette/roulette/table.py


class InvalidBet(Exception):
    pass


class Table():
    """
    Table contains all the Bet s created by the Player.

    A table also has a betting limit, and the sum of all of a players bets
    must be less than or equal to this limit.
    """

    def __init__(self):

        self.limit = 1000000
        self.bets = []

    def __iter__(self):
        for bet in self.bets:
            yield bet

    def __str__(self):
        return ", ".join(self.bets)

    def __contains__(self, bet):
        return bet in self.bets

    def isValid(self, bet):
        """Validates this bet.

        If the sum of all bets is less than or equal to the table limit, then
        the bet is valid, return true. Otherwise, return false.

        Args:
            bet: A Bet instance to be validated.
        """
        return bet.getAmount() < self._remaining_bets_limit()

    def placeBet(self, bet):
        """Adds this bet to the list of working bets.

        If the sum of all bets is greater than the table limit, then an
        exception should be thrown (Java) or raised (Python). This is a rare
        circumstance, and indicates a bug in the Player more than anything
        else.

        Args:
            bet: A Bet instance to be validated.
        Raises:
            InvalidBet
        """

        # check if the bet is valid first
        if self.isValid(bet):
            self.bets.append(bet)

        else:
            raise InvalidBet

    def cleanTable(self):
        """Delete all bets in table."""
        self.bets = []

    def removeBet(self, bet):
        """Remove bet from the table.

        Args:
            bet: A bet that has to be removed from table.
        """
        self.bets.remove(bet)

    def isEmpty(self):
        return self.bets == []

    def _remaining_bets_limit(self):
        """Calculates how much bets amount can be placed."""

        total_bets_amount = sum(bet.getAmount() for bet in self.bets)

        return self.limit - total_bets_amount
