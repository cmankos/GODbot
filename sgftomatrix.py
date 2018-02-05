import os
import glob
import pickle


def sgfToMatrix(sgfContents, name):
    """
    Function to turn a sgf Go file to a dictionary containing the finalized board state, and the
    path that both the white player and the black player will take
    :param sgfContents: The contents of the .sgf file
    :param name: The name of the file
    :return: A dictionary of data of the sgf
    """
    # Create the return dictionary
    endState = dict()
    # Fill in the name which is the file of the sgf
    endState["name"] = name[0:-4]
    # Fill three blank arrays to keep the board, and two paths in
    board = [[0 for x in range(19)] for y in range(19)]
    blackPath = [[None for x in range(19)] for y in range(19)]
    whitePath = [[None for x in range(19)] for y in range(19)]
    # Two iterators for the paths
    blackPathIt = 0
    whitePathIt = 0
    # We go from 2 onwards bc 0 and 1 are just setting stuff up
    for line in sgfContents.split(";")[2:]:
        # If the line is a black stone
        if line[0:1] == "B":
            # Get the i and j coords
            i = ord(line[2]) - ord("a")
            j = ord(line[3]) - ord("a")
            # Put a one in the board bc it is a black stone
            board[i][j] = 1
            # Add to the path and increment the iterator
            blackPath[i][j] = blackPathIt
            blackPathIt += 1
            # Continue onto the next loop
            continue

        elif line[0:1] == "W":
            # Same logic as above
            i = ord(line[2]) - ord("a")
            j = ord(line[3]) - ord("a")
            board[i][j] = 2
            whitePath[i][j] = whitePathIt
            whitePathIt += 1
            continue

        # If it is a AB then the game has a handicap and we don't want it
        elif line[0:2] == "AB":
            return None

    # Set up the dictionary
    endState["board"] = board
    endState["winner"] = sgfContents.split(";")[1].split("RE")[-1].split("]")[0][1:]
    endState["blackPath"] = blackPath
    endState["whitePath"] = whitePath

    # Return the dictionary
    return endState

# Create a list of all teh end states
endStates = []
# Change the dir to the 9p player files
os.chdir("./sgf/9p")
# Go through all of the files
for file in glob.glob("*.sgf"):
    # Open all of the files
    with open(file) as game:
        # Convert it to a dict
        endState = sgfToMatrix(game.read(), game.name)
        # Append it to the end states
        endStates.append(endState)

# Go through each end state
for endState in endStates:
    # If it is not none
    if endState is not None:
        # Pickle dump to a different file location
        with open("../../matrix/9p/{}.p".format(endState["name"]), 'wb') as handle:
            pickle.dump(endState, handle, protocol=pickle.HIGHEST_PROTOCOL)

