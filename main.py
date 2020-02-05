import sys
from game import Game

if __name__ == '__main__':
    with open(sys.argv[1]) as fil:
        for line in fil.readlines()[:1]:
            num_list = line.split(' ')
            num_rows = num_list[0]
            num_cols = num_list[1]
            num_rows = int(num_rows)
            num_cols = int(num_cols)

    #board_dim = 3
    #if len(sys.argv) >= 2:  # user provided a board dimension
        #board_dim = sys.argv[1]
    game = Game(num_rows, num_cols)
    game.play()
