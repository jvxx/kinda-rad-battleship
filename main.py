import sys
from game import Game

if __name__ == '__main__':
    '''
    board_dim = 1
    if len(sys.argv) >= 2:  # user provided a board dimension
        with open(sys.argv[1]) as fil:
            for line in fil.readlines()[:1]:
                num_rows, num_cols = line[0], line[1]
        board_dim = num_rows, num_cols
    game = Game(board_dim)
    board = Board()
    Game(sys.argv[1])
    game.play()
    '''

    board_dim = 3
    if len(sys.argv) >= 2:  # user provided a board dimension
        board_dim = int(sys.argv[1])
    game = Game(board_dim)
    game.play()