"""File that creates a bunch of teensy weensies and fights them and then mates them"""

import Genetic1.py
import random

POP = 10000  # population size
BATTLEROYAL = 100000 # How many times each generation fights. Probably high but gets a good smattering at least?


def main():

    teensies = []   # list of our bots

    # Adds POP number of bots to our list
    for i in range(POP):
        teensies += Genetic1.ThrownToTheBoard()

    for i in range(BATTLEROYAL):
        fight(teensies(random.randint(0, POP)), teensies(random.randint(0, POP)))
        # Would like to change score so it subtracts score from loser as well? Then multiplying doesn't work

    mate()

    return 0















