# roulette/roulette/wheel.py


from roulette.bin import Bin
import random
from roulette.bin_builder import BinBuilder


class Wheel(object):

    def __init__(self, rng=None):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng or random.Random()
        self.all_outcomes = {}
        self._build_bins()

    def add_outcome(self, number, outcome):
        """Add outcome to a specified bin.

        Args:
            number: Bin number (0 to 37).
            outcome: Outcome to be added to the Bin."""

        # add outcome to its bin
        self.bins[number].add(outcome)

        # add outcome to a dictionary
        self.all_outcomes[outcome.getName()] = outcome

    def next(self):
        """Generates random number between 0 and 37, and returns that Bin."""

        return self.bins[self.rng.choice(range(38))]

    def get(self, number):
        """Returns the Bin of that number."""

        return self.bins[number]

    def get_outcome(self, name):
        """Returns a reference to an outcome mapped in the wheel."""

        # check if the outcome is mapped
        if name in self.all_outcomes:
            return self.all_outcomes[name]

        else:
            return None

    def _build_bins(self):
        """Build bins of the wheel."""

        bin_builder = BinBuilder()
        bin_builder.build_bins(self)
