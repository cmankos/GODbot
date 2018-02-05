import os
import glob


def sgfToMatrix(sgfContents):
    board = [[0 for x in range(19)] for y in range(19)]
    # We go from 2 onwards bc 0 and 1 are just setting stuff up
    for line in sgfContents.split(";")[2:]:
        if line[0:1] == "B":
            i = ord(line[2]) - ord("a")
            j = ord(line[3]) - ord("a")
            board[i][j] = 1
            continue
        elif line[0:1] == "W":
            try:
                i = ord(line[2]) - ord("a")
                j = ord(line[3]) - ord("a")
                board[i][j] = 2
                continue
            except IndexError:
                print("{}, {}".format(i, j))

        elif line[0:2] == "AB":
            stonesToAdd = line[2:].split("]")
            for line in stonesToAdd[0:len(stonesToAdd) - 1]:
                line = line[1:]
                i = ord(line[0]) - ord("a")
                j = ord(line[1]) - ord("a")
                board[i][j] = 1
                continue
    return board


endStates = []
os.chdir("./sgf/9p")
for file in glob.glob("*.sgf"):
    with open(file) as game:
        endStates.append(sgfToMatrix(game.read()))

os.chdir("../../matrix/9p/")
for x in range(len(endStates)):
    with open("{}.txt".format(x), "w+") as file:
        for line in endStates[x]:
            file.write(str(line))
            file.write("\n")

