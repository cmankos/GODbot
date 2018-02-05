"""
First genetic algorithm for the go board. Very fast, very loose, rewarding based on how close a particular board
reaches a desired end board state (chosen from a database)
"""

import random

class ThrownToTheBoard():

    def __init__(self, pBoard, pColor, pPath, pIdeal, pBoardSize = 19):
        self.board = pBoard # current board state, NOT the idealized board
        self.color = pColor # which color stones you're placing down
        self.boardSize = pBoardSize # 19x19 is traditional size
        self.ideal = pIdeal # what we're trying to attain
        self.path = pPath   # order of stones to play in


    # Rewrite, takes in 2 parents' paths
    # Takes 2 parents and produces an offspring board
    def mate(self, parent1, parent2):

        for x in range(self.boardSize):
            for y in range(self.boardSize):
                if random.random() >= 0.5:
                    self.path[x][y] = parent1[x][y]
                else:
                    self.path[x][y] = parent2[x][y] + 0.5

        self.rescale()

        self.mutate()

    # Terribly inefficient. Someone magic this away. It disgusts me
    # Takes the board and puts rearranges its elements into the natural numbers
    def rescale(self):

        i = 501

        # makes all 0's 500 so they aren't the min, 500 chosen because 500 > 361
        for x in range(self.boardSize):
            for y in range(self.boardSize):
                if self.path[x][y] == 0:
                    self.path[x][y] = 500


    # Randomly switches the board's squares to something else
    def mutate(self):

        MUTATE = .0001           # mutation rate
        STONES = [0, 1, 2]

        for x in range(self.boardSize):
            for y in range(self.boardSize):
                if random.random() < MUTATE:
                    self.board[x][y] = random.choice(STONES)



    # Compares attained board against idealized board - 1 for match, -1 for miss, 0 else)
    def score(self, scoreboard):

        for x in range(self.boardSize):
            for y in range(self.boardSize):
                k = scoreboard[x][y]
                # If the board's stone matches the idealized board's,
                if self.board[x][y] == k and self.color == scoreboard[x][y]:



















