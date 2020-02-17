import sys
from game import Game

if __name__ == '__main__':
    with open(sys.argv[1]) as fil:
        for line in fil.readlines()[:1]:
            num_list = line.split(' ')
            num_rows = int(num_list[0])
            num_cols = int(num_list[1])
    random_seed = int(sys.argv[2])
    game = Game(num_rows, num_cols, random_seed)
    game.play()
