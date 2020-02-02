from typing import Iterable, TypeVar
import sys
from player import Player
from board import Board

T = TypeVar('T')

class Game(object):

    def __init__(self):
        self.turn = Player.turn(self)

        ...

    def open_coords_configs(filepath = sys.argv[1]):
        with open(sys.argv[1]) as fil:
            for line in fil.readlines()[:1]:
                num_rows, num_cols = line[0], line[2]
                player_board = Board(num_rows, num_cols)
            return player_board.display_board()


    def open_ship_configs(filepath = sys.argv[1]):
        with open(sys.argv[1]) as fil:
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]
            for i in all_these_ships:
                ship_name, ship_length = i[0], i[1]
                return ship_name, ship_length

    def setup(self):
        '''
        opening and parsing files -> rows/cols, and ship name/ship length

        with open(sys.argv[1]) as fil:
            for line in fil.readlines()[:1]:
                num_rows, num_cols = line[0], line[1]
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]
            for i in all_these_ships:
                ship_name, ship_length = i[0], i[1]

        '''

        self.open_coords_configs()
        self.open_ship_configs()
        self.get_players()
        self.turn
        ...

    def get_players(self):
        self.Player.get_player_name()
        ...

    def play(self):
        while not self.gameover():
            Player.turn(self)
        ...

    def win(self):
        ...

    def gameover(self):
        return self.win()

if __name__ == '__main__':
    test = Game()

    print(test.setup())