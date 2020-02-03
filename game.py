from typing import Iterable, TypeVar
import sys
from player import Player
from board import Board
from ship import Ship

T = TypeVar('T')

class Game(object):

    def __init__(self, dim):
        #self.turn = Player.turn(self, board)
        #self.board = self.open_coords_configs()
        self.board = self.open_coords_configs()
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players))
        self._cur_player_turn = 0

        ...


    def open_coords_configs(filepath = sys.argv[1]):
        with open(sys.argv[1]) as fil:
            for line in fil.readlines()[:1]:
                num_rows, num_cols = line[0], line[2]
                player_board = Board(num_rows, num_cols)
            return player_board.display_board()


    '''
    def open_ship_configs(filepath = sys.argv[1]):
        ship_name_list = []
        ship_length_list = []
        with open(sys.argv[1]) as fil:
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]

            ship_names, ship_lengths = zip(*all_these_ships)

            for name in ship_names:
                ship_name_list.append(name)
            #print(ship_name_list)

            for length in ship_lengths:
                ship_length_list.append(length)
            #print(ship_length_list)

            for i, name in enumerate(ship_name_list):
                print(name, i)

            return ship_name_list, ship_length_list
    '''

            
    '''
    def attain_ships(self):
        sdfas = self.open_ship_configs()
        print(sdfas)
        #for ship_name, ship_length in sdfas:
            #player_ships = Ship(ship_name, ship_length)
            #return player_ships.ship_name()
    '''

    def setup(self):
        #self.turn()
        #self.open_coords_configs()
        #self.open_ship_configs()
        #self.attain_ships()
        #self.get_players()
        ...

    def get_players(self):
        # self.players starts as an empty list, then for i in range(2): we append each player to our list
        our_players = [Player(self.players) for i in self.players]

        name_player_map = {}

        for index, i in enumerate(our_players):
            if index == 0:
                name_player_map[i] = 1
            elif index == 1:
                name_player_map[i] = 2
        return name_player_map

        ...


    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2


    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]


    def play(self):
        #self.open_coords_configs()
        while not self.gameover():
            self.cur_player.turn(self.board)
            self.change_turn()

        self.change_turn()

            #self.open_ship_configs()
            #Player.turn(self)
            #self.cur_player.take_turn(self.board)
        ...

    def win(self):
        ...

    def gameover(self):
        return self.win()

if __name__ == '__main__':
    #board = Board(5, 5)
    test = Game(5)

    print(test.play())