import sys
from typing import Iterable
from board import Board
from ship import Ship

import abc

class Player(abc.ABC):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        self.blank_char = blank_char
        self.board = Board(row, col, blank_char)
        # self.player_type = self.get_player_type(player_num)
        self.name = self.get_player_name(player_num, other_players)
        self.ship_list = self.get_player_ship()
        self.ship_placement = self.get_ship_placement()


    @abc.abstractmethod
    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        ...

    @abc.abstractmethod
    def get_player_ship(self):
        ...

    @abc.abstractmethod
    def get_ship_orient(self, ship) -> str:
        ...

    def initial_player_board(self):
        # for placing ships
        for i in range(2):
            if i == 0:
                pass
            elif i == 1:
                print(f"{self.name}'s Placement Board")
                print(" ", end='')
                for col_num in range(self.col):
                    print(" " + str(col_num), end='')
                print()
                for row_num in range(self.row):
                    print(row_num, end='')
                    for col_num in range(self.col):
                        print(" " + self.board.contents[i][row_num][col_num], end='')
                    print()

    def get_player_board(self):
        # for shooting ships
        for i in range(2):
            if i == 0:
                print(f"{self}'s Scanning Board")
            elif i == 1:
                print(f"{self}'s Board")
            print(" ", end='')
            for col_num in range(self.col):
                print(" " + str(col_num), end='')
            print()
            for row_num in range(self.row):
                print(row_num, end='')
                for col_num in range(self.col):
                    print(" " + self.board.contents[i][row_num][col_num], end='')
                print()
            print()

    @abc.abstractmethod
    def get_ship_placement(self):
        ...
        # WE NEED THE PLACEMENT BOARD HERE
        # self.initial_player_board()
        #
        # self.initial_player_board()

    @abc.abstractmethod
    def shoot(self, row: int, col: int) -> bool:
        ...

    @abc.abstractmethod
    def turn(self, other_player):
        ...
        # self.get_player_board()
        #
        # hit = other_player.shoot(row, col)
        #
        # # mark scanning boards accordingly
        # if hit:
        #     self.board.contents[0][row][col] = 'X'
        # else:
        #     self.board.contents[0][row][col] = 'O'
        #     print('Miss')
        #
        # self.get_player_board()

    def __str__(self) -> str:
        # convert player name from weird object thing to str
        return self.name
