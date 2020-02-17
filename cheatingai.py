import sys
import random
from typing import Iterable
from ship import Ship
from player import Player
from aiplayer import AIPlayer
from board import Board
from coordinates import Coordinates

# command line args: configs/minor_game.txt 75

class CheatingAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)
        # self.row_list = self.stolen_rows()
        # self.col_list = self.stolen_cols()

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Cheating Ai {playerNum}"
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

    def stealin_my_coords(self):
        super().stealin_my_coords()




    def shoot(self, row: int, col: int) -> bool:
        ship_initial = self.board.contents[1][row][col]
        for ship in self.ship_list:
            if ship.name[0] == ship_initial:
                self.board.contents[1][row][col] = 'X'
                ship.got_hit(self.name)
                return True

    def turn(self, other_player):
        self.get_player_board()
        loser = other_player.stealin_my_coords()

        stole_their_coords = loser
        print(stole_their_coords)
        cur_coords = stole_their_coords.pop(0)
        # self.ship_coords.remove(cur_coords)

        row = cur_coords[0]
        col = cur_coords[1]

        print(row, col)

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
