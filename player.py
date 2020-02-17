import sys
from typing import List
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
        self.name = self.get_player_name(player_num, other_players)
        self.ship_list = self.get_player_ship()
        self.ship_placement = self.get_ship_placement()

    @abc.abstractmethod
    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        ...

    def get_player_ship(self) -> List[Ship]:
        """
        create a pretty cool list of all our ships
        """
        ship_list = []
        with open(sys.argv[1]) as fil:
            for s in fil.readlines()[1:]:
                s = s.split(' ')
                ship_name = s[0]
                ship_length = int(s[1])
                ship_list.append(Ship(ship_name, ship_length))

            return ship_list

    def initial_player_board(self):
        """
        this is the creation of the placement board
        """
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
        """
        and these are the boards used in game--
        where board[0] corresponds to the scanning board,
        and board[1] corresponds to the player's own board
        """
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

    def shoot(self, row: int, col: int) -> bool:
        """
        this is checking the board of the player who's being shot at (ie not the player in the current turn)

        check if the coordinates contains a ship,
        and return False if there is no ship.
        if there is a ship,
        look up which ship the initials correspond to, mark an X, and return True
        """
        if self.board.contents[1][row][col] == '*':
            self.board.contents[1][row][col] = 'O'
            return False
        elif self.board.contents[1][row][col] == 'X':
            return False
        elif self.board.contents[1][row][col] == 'O':
            return False
        else:
            ship_initial = self.board.contents[1][row][col]
            for ship in self.ship_list:
                if ship.name[0] == ship_initial:
                    self.board.contents[1][row][col] = 'X'
                    ship.got_hit(self.name)
                    return True

    @abc.abstractmethod
    def turn(self, other_player):
        ...

    def __str__(self) -> str:
        """
        convert player name from weird object thing to str
        """
        return self.name
