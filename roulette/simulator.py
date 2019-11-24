# roulette/roulette/simulator.py


from roulette.game import Game
from roulette.player import Martingale
from roulette.wheel import Wheel
from roulette.table import Table


class Simulator():
    """
    Simulator runs a game of Roulette for a given player that bets.
    It calculates and displays statistics on a number of sessions of play.
    """

    INIT_DURATION = 250
    INIT_STAKE = 100
    SAMPLES = 100

    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.maximum = []
        self.final = []
        self.durations = []

    def session(self):
        """
        Runs a single game.

        1. The Player is initialized with their initial stake and # of cycles to run
        2. An empty List of stake values is created.
        3. The session loop runs until the Player playing() returns false.
        4. Loops the Game cycle() then it gets the stake from the Player and appends to list of stake values.
        5. List of individual stake values is returned as the result of the session of play.

        Returns:
            List of stake values.
        """

        stakes = []

        # init player
        self.player.setRoundsToGo(self.INIT_DURATION)
        self.player.setStake(self.INIT_STAKE)

        # cycle the game while player is active
        while self.player.playing():
            self.game.cycle(self.player)

            # append stake value to the list
            stakes.append(self.player.getStake())

        return stakes

    def gather(self):
        """
        Executes the number of games sessions in samples.

        1. Each session() returns a list of stake values at end of session
                - play reached their time limit
                - stake was spent.
        2. The resulting metric is: maximum value, final value, length of list.
        3. Resulting metrics are appended to the durations, maximum and final
        lists.
        """

        for i in range(self.SAMPLES):

            print("Running session: " + str(i + 1))
            stakes = self.session()

            # extract metrics from stakes list
            max_value = max(stakes)
            final_value = stakes[-1]
            duration = len(stakes)

            # append to lists gathering metrics
            self.maximum.append(max_value)
            self.final.append(final_value)
            self.durations.append(duration)


def main():

    # create game and player
    wheel = Wheel()
    table = Table()
    game = Game(wheel, table)
    player = Martingale(table)

    # create simulator instance
    simulator = Simulator(game, player)
    simulator.gather()

    # print results
    print("Maximum", simulator.maximum, "\n")
    print("Final", simulator.final, "\n")
    print("Durations", simulator.durations, "\n")


if __name__ == '__main__':
    main()
