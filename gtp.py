from subprocess import Popen, PIPE
from enum import Enum


class MoveStatus(Enum):
    VALID_MOVE = 1
    INVALID_MOVE = 2
    INVALID_COORD_OR_COLOR = 3
    ERROR = 4


class GNUGo:
    """
    A class that can connect to gnugo in gtp mode and send some commands and return
    some stuff
    """
    def __init__(self, boardsize=9):
        """
        Constructor that connects to the gnugo using pipes
        :param boardsize: (int) size of the board, usually 9, 13, or 19
        """
        # Connect to gnugo in gtp mode
        self.gnuGo = Popen(['./gnugo/gnugo.exe', '--mode', 'gtp'], stdin=PIPE, stdout=PIPE)

    # Private send method (We are all adults here)
    def _send(self, data_to_send):
        """
        Private method to send data and recieve data from the gtp protocol
        of gnuGo. Raises a ValueError if there are any problems with communication
        or the inputted command
        :param data_to_send: (string) Command to send to gnuGo
        :return: (string) The return from gnuGo
        """
        # Get the return and error from the communication
        out, err = self.gnuGo.communicate(bytes(data_to_send, "UTF-8"))
        # If there was an error raise an exception
        if err is not None:
            # Return a ValueError
            raise ValueError("There was a problem with the communication")

        # If there was no error
        else:
            # Check the first char in the return, if it is a "?" then there was a problem
            if out[0] == "?":
                return out
            # Else if the command was good
            else:
                # Return from 1 onwards
                return str(out[2:], "UTF-8")

    def send_move(self, col, row, color):
        """
        Public method to send a move to gnuGo
        :param col: (char) Column of the move
        :param row: (int) Row of the move
        :param color: (string) color to move, either white or black
        :return: (boolean) True if the move was successful, false otherwise
        """
        # Try to send the move over the pipe
        try:
            # Construct the command and send it
            out = self._send("play {0} {1}{2}".format(color, col, row))
            if out[0] == "?":
                if out == "? illegal move":
                    return MoveStatus.INVALID_MOVE
                elif out == "? invalid color or coordinate":
                    return MoveStatus.INVALID_COORD_OR_COLOR
            # If the sending was successful then return true
            return MoveStatus.VALID_MOVE
        except ValueError:
            # Return false on any ValueError
            return MoveStatus.ERROR

    def get_move(self, color):
        """
        Public method to generate a move for either color
        :param color: (string) color to generate for, either white or black
        :return: (string) The row and column of the move, ex. C7
        """
        try:
            # Construct the command and get the top line
            return self._send("genmove {0}".format(color)).split("\n")[0]
        except ValueError:
            # Return false on any ValueError
            return False

    def estimate_score(self):
        """
        Public method that returns the score estimation from GNUGo
        :return: A dictionary with the score and color in their respective
        indexes, the score has a sign. Ex. {color: w, score: +0.00}
        """
        try:
            # Get the entire score estimate but only store the first line
            score_est = self._send("estimate_score").split()[0]
            # Create a dict to return
            ret_score = dict()
            # Store the color and the score
            ret_score["color"] = score_est[0]
            ret_score["score"] = score_est[1:]
            # Return the dictionary
            return ret_score
        except ValueError:
            # Return false on any ValueError
            return False
