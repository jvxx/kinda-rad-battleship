import sys
from game import Game

if __name__ == '__main__':
    with open(sys.argv[1]) as fil:
        for line in fil.readlines()[:1]:
            num_rows, num_cols = line[0], line[2]
            num_rows = int(num_rows) + 1
            num_cols = int(num_cols) + 1

    #board_dim = 3
    #if len(sys.argv) >= 2:  # user provided a board dimension
        #board_dim = sys.argv[1]
    game = Game(num_rows, num_cols)
    game.start_up()
    #game.play()
