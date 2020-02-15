import sys
import random
from typing import Iterable
from ship import Ship
from player import Player
from aiplayer import AIPlayer
from board import Board
from coordinates import Coordinates


class CheatingAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)
        # self.row_list = self.stolen_rows()
        # self.col_list = self.stolen_cols()

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Cheating AI {playerNum}"
        return name

    def get_player_ship(self):
        ship_list = []
        with open(sys.argv[1]) as fil:
            for s in fil.readlines()[1:]:
                s = s.split(' ')
                ship_name = s[0]
                ship_length = int(s[1])
                ship_list.append(Ship(ship_name, ship_length))

            return ship_list

    def get_ship_orient(self, ship):
        super().get_ship_orient(ship)

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

    def get_ship_placement(self):
        self.initial_player_board()
        super().get_ship_placement()
        self.initial_player_board()

    def stealin_my_coords(self):
        ship_row_coords = []
        ship_col_coords = []

        # ship_coords = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.contents[1][row][col] != '*':
                    # row = int(row)
                    # col = int(col)
                    # ship_coords.append(Coordinates(row, col))

                    ship_row_coords.append(row)
                    ship_col_coords.append(col)
        ship_coords = list(zip(ship_row_coords, ship_col_coords))
        # print(ship_coords)
        return ship_coords

    # these are creating a new list and so they're returning the same value every time
    # if we return rad_rows.pop(0)
    # so gotta add it to the constructor
    def stolen_rows(self):
        took_their_coords = self.stealin_my_coords()
        rad_rows = []
        for i in took_their_coords:
            row = i[0]
            row = int(row)
            rad_rows.append(row)
        return rad_rows
        # return rad_rows.pop(0)

    def stolen_cols(self):
        took_their_coords = self.stealin_my_coords()
        cool_cols = []
        for i in took_their_coords:
            col = i[1]
            col = int(col)
            cool_cols.append(col)
        return cool_cols
        # return cool_cols.pop(0)


    def shoot(self, row: int, col: int) -> bool:
        ship_initial = self.board.contents[1][row][col]
        for ship in self.ship_list:
            if ship.name[0] == ship_initial:
                self.board.contents[1][row][col] = 'X'
                ship.got_hit(self.name)
                return True

    def turn(self, other_player):
        self.get_player_board()
        row = other_player.row_list.pop(0)
        col = other_player.col_list.pop(0)
        # print(row)
        # print(col)
        hit = other_player.shoot(row, col)
        if hit:
            self.board.contents[0][row][col] = 'X'
        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()

    def __str__(self) -> str:
        # convert player name from weird object thing to str
        return self.name
