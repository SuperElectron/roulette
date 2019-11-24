# roulette/roulette/bin_builder.py


from roulette.roulettePayout import RoulettePayout
from roulette.outcome import Outcome


class BinBuilder():
    """
    Build up Bins of a Wheel, filling them with its Outcomes.

    Calls one method for each kind of bet in bet_methods attribute.
    Place Outcomes in bin by iterating through Wheel Bins that have Outcomes on a bet
    """

    RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21,
                   23, 25, 27, 30, 32, 34, 36]

    def __init__(self):
        self.bet_methods = (self._gen_straight, self._gen_split,
                            self._gen_street, self._gen_corner, self._gen_line,
                            self._gen_dozen, self._gen_column, self._gen_even,
                            self._gen_five)

    def buildBins(self, wheel):
        """Fill Bins of a Wheel with Outcomes of each kind of bet."""

        # iterate all bet building methods
        for bet_method in self.bet_methods:
            bet_method(wheel)

    def _gen_straight(self, wheel):
        """Generate all straight bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.StraightBet

        # create and assign outcomes for numbers from 1 to 36
        for i in range(1, 37):

            # create outcome
            outcome_name = "Number " + str(i)
            outcome = Outcome(outcome_name, outcome_odds)

            # assign to bin
            wheel.add_outcome(i, outcome)

        # create zero outcome and assign it to 0 bin
        outcome_name = "Number 0"
        outcome = Outcome(outcome_name, outcome_odds)
        wheel.add_outcome(0, outcome)

        # create double zero outcome and assign it to 00 bin
        outcome_name = "Number 00"
        outcome = Outcome(outcome_name, outcome_odds)
        wheel.add_outcome(37, outcome)

    def _gen_split(self, wheel):
        """Generate all split bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.SplitBet

        # create all left-right split bets iterating all rows and first 2 cols
        for row in range(12):
            for col in range(1, 3):

                # create outcome
                left_num = 3 * row + col
                right_num = left_num + 1
                outcome_name = "Split {}-{}".format(left_num, right_num)
                outcome = Outcome(outcome_name, outcome_odds)

                # assign outcome to bins
                wheel.add_outcome(left_num, outcome)
                wheel.add_outcome(right_num, outcome)

        # create all up-down split bets iterating first 11 rows and all cols
        for row in range(11):
            for col in range(1, 4):
                up_num = 3 * row + col
                down_num = up_num + 3
                outcome_name = "Split {}-{}".format(up_num, down_num)
                outcome = Outcome(outcome_name, outcome_odds)

                # assign outcome to bins
                wheel.add_outcome(up_num, outcome)
                wheel.add_outcome(down_num, outcome)

    def _gen_street(self, wheel):
        """Generate all street bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.StreetBet

        # create and assign one street bet per row
        for row in range(12):

            # calculate the numbers of the row
            nums = [3 * row + 1,
                    3 * row + 2,
                    3 * row + 3]

            outcome_name = "Street {}-{}-{}".format(nums[0], nums[1], nums[2])
            outcome = Outcome(outcome_name, outcome_odds)

            # assign outcome to bins
            for num in nums:
                wheel.add_outcome(num, outcome)

    def _gen_corner(self, wheel):
        """Generate all corner bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.CornerBet

        # create all corner bets iterating first 11 rows and first 2 columns
        for row in range(11):
            for col in range(2):

                # calculate the numbers of the corner bet
                nums = [3 * row + 1 + col,
                        3 * row + 2 + col,
                        3 * row + 4 + col,
                        3 * row + 5 + col]

                outcome_name = "Corner {}-{}-{}-{}".format(nums[0], nums[1],
                                                           nums[2], nums[3])
                outcome = Outcome(outcome_name, outcome_odds)

                # assign outcome to bins
                for num in nums:
                    wheel.add_outcome(num, outcome)

    def _gen_line(self, wheel):
        """Generate all line bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.LineBet

        # create and assign one line bet per row (iter only first 11 rows)
        for row in range(11):

            # calculate the numbers of the line (2 rows)
            nums = [3 * row + 1,
                    3 * row + 2,
                    3 * row + 3,
                    3 * row + 4,
                    3 * row + 5,
                    3 * row + 6]

            outcome_name = "Line {}-{}-{}-{}-{}-{}".format(nums[0], nums[1],
                                                           nums[2], nums[3],
                                                           nums[4], nums[5])
            outcome = Outcome(outcome_name, outcome_odds)

            # assign outcome to bins
            for num in nums:
                wheel.add_outcome(num, outcome)

    def _gen_dozen(self, wheel):
        """Generate all dozen bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.DozenBet

        # create and assign a dozen bet for each number
        for dozen in range(3):

            outcome_name = "Dozen " + str(dozen + 1)
            outcome = Outcome(outcome_name, outcome_odds)

            # assign outcome to bins
            for num in [i + (12 * dozen) for i in range(1, 13)]:
                wheel.add_outcome(num, outcome)

    def _gen_column(self, wheel):
        """Generate all column bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.ColumnBet

        # create and assign a dozen bet for each number
        for col in range(1, 4):

            outcome_name = "Column " + str(col)
            outcome = Outcome(outcome_name, outcome_odds)

            # assign outcome to bins
            for num in [i * 3 + col for i in range(12)]:
                wheel.add_outcome(num, outcome)

    def _gen_even(self, wheel):
        """Generate all even bets and assign them to bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.EvenBet

        outcome_low = Outcome("Low", outcome_odds)
        outcome_high = Outcome("High", outcome_odds)
        outcome_even = Outcome("Even", outcome_odds)
        outcome_odd = Outcome("Odd", outcome_odds)
        outcome_red = Outcome("Red", outcome_odds)
        outcome_black = Outcome("Black", outcome_odds)

        # iterate all numbers assining corresponding even bets
        for num in range(1, 37):

            # assign low-high bets
            if num < 19:
                wheel.add_outcome(num, outcome_low)
            else:
                wheel.add_outcome(num, outcome_high)

            # assign even-odd bets
            if num % 2 == 0:
                wheel.add_outcome(num, outcome_even)
            else:
                wheel.add_outcome(num, outcome_odd)

            # assign even-odd bets
            if num in self.RED_NUMBERS:
                wheel.add_outcome(num, outcome_red)
            else:
                wheel.add_outcome(num, outcome_black)

    def _gen_five(self, wheel):
        """Generate five bet and assign them to its bins."""

        # retrieve outcome odds for this bet
        outcome_odds = RoulettePayout.FiveBet
        outcome = Outcome("00-0-1-2-3", outcome_odds)

        # assign to bins
        for num in [0, 37, 1, 2, 3]:
            wheel.add_outcome(num, outcome)
