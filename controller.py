from gtp import GNUGo

gnuGo = GNUGo(boardsize=9)
print(gnuGo._send("showboard"))