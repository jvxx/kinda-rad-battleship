import sys
from typing import Iterable, TypeVar
from player import Player
from board import Board
from ship import Ship

T = TypeVar('T')

class Game(object):

    def __init__(self, row, col, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        #self.blank_char = blank_char
        self.board = Board(row, col, blank_char)
        self.player_board = Player.get_player_board(self)
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players, row, col, blank_char))
        self._cur_player_turn = 0

        ...


    '''
    def open_coords_configs(filepath = sys.argv[1]):
        with open(sys.argv[1]) as fil:
            for line in fil.readlines()[:1]:
                num_rows, num_cols = line[0], line[2]
                #player_board = Board(num_rows, num_cols)
            return num_rows, num_cols
    '''

    def display_current_board(self) -> None:
        ...
        #print(self.board)


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

    def start_up(self) -> None:
        self.player_board
        while True:
            self.cur_player.initial_turn(self.player_board, self.row, self.col)


    def play(self) -> None:
        while not self.gameover():
            self.display_current_board()
            self.cur_player.initial_turn(self.player_board)
            self.change_turn()

        # last player will always be the losing player
        # so gotta switch back to correct player
        self.change_turn()
        self.display_current_board()

            #self.open_ship_configs()
            #Player.turn(self)
            #self.cur_player.take_turn(self.board)
        ...

    def win(self):
        ...

    def gameover(self):
        return self.win()
