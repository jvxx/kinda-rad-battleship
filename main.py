import sys
import random
from game import Game
from player import Player
from humanplayer import HumanPlayer
from cheatingai import CheatingAI

if __name__ == '__main__':
    with open(sys.argv[1]) as fil:
        for line in fil.readlines()[:1]:
            num_list = line.split(' ')
            num_rows = num_list[0]
            num_cols = num_list[1]
            num_rows = int(num_rows)
            num_cols = int(num_cols)
    # random.seed(sys.argv[2])

    game = Game(num_rows, num_cols)
    game.play()
