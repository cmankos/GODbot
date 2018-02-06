"""
First genetic algorithm for the go board. Very fast, very loose, rewarding based on how close a particular board
reaches a desired end board state (chosen from a database)
"""

import random

class ThrownToTheBoard:

    def __init__(self, pBoard, pColor, pPath, pIdeal, pBoardSize = 19):
        self.board = pBoard # current board state, NOT the idealized board
        self.color = pColor # which color stones you're placing down
        self.boardSize = pBoardSize # 19x19 is traditional size
        self.path = pPath   # order of stones to play in


    # Takes 2 parents and produces an offspring board
    def mate(self, parent1, parent2):
        # since everything else is random, why not this?

        # Randomly choose a crossover point
        if random.random() <= 0.5:
            k = random.randint(len(parent1.board))
            self.board = parent1.board[0:k+1] + parent2.board[k:]

        else:
            k = random.randint(len(parent2.board))
            self.board = parent2.board[0:k+1] + parent2.board[k:]

        self.mutate()


    # Randomly switches the board's squares to something else
    def mutate(self):
        """
        Mutates the dna by randomly swapping two elements of the path
        :return: None
        """
        mutate = .0001           # mutation rate
        if random.random() < mutate:
            # Chris cross!
            i = random.randrange(0, len(self.path))
            j = random.randrange(0, len(self.path))
            # One hop this time
            self.path[i], self.path[j] = self.path[j], self.path[i]



    # Compares attained board against idealized board - 1 for match, -1 for miss, 0 else)
    def score(self, score):
        




















