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
        # self.blank_char = blank_char
        # self.board = Board(row, col, blank_char)
        # self.player_board = Player.get_player_board(self)
        self.players = []
        for player_num in range(1,3):
            self.players.append(Player(self.players, row, col, player_num, blank_char))
        self._cur_player_turn = 0

        ...

    # def get_players(self):
    #     # self.players starts as an empty list, then for i in range(2): we append each player to our list
    #     our_players = [Player(self.players) for i in self.players]
    #
    #     name_player_map = {}
    #
    #     for index, i in enumerate(our_players):
    #         if index == 0:
    #             name_player_map[i] = 1
    #         elif index == 1:
    #             name_player_map[i] = 2
    #     return name_player_map

        ...

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def play(self):
        while not self.game_over():
            self.cur_player.turn(self.players[(self._cur_player_turn + 1) % 2])
            self.change_turn()
        self.change_turn()
        print(
            f'{self.cur_player.name} won the game!'
        )
        ...

    def game_over(self):
        for ship in self.cur_player.ship_list:
            if ship.length != 0:
                return False
        return True
