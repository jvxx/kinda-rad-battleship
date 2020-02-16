import sys
import random
from typing import Iterable
from ship import Ship
from player import Player
from aiplayer import AIPlayer

# command line args: configs/minor_game.txt 89

class RandomAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Random Ai {playerNum}"
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
        ship_row_coords = []
        ship_col_coords = []

        # ship_coords = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                ship_row_coords.append(row)
                ship_col_coords.append(col)
        ship_coords = list(zip(ship_row_coords, ship_col_coords))
        # print(ship_coords)
        return ship_coords

    def stolen_rows(self):
        took_my_coords = self.stealin_my_coords()
        rad_rows = []
        for i in took_my_coords:
            row = i[0]
            row = int(row)
            rad_rows.append(row)
        rad_rows.sort()
        # cur_row = random.choice(rad_rows)
        # cur_row = int(cur_row)
        # rad_rows.remove(cur_row)
        return rad_rows

    def stolen_cols(self):
        took_my_coords = self.stealin_my_coords()
        cool_cols = []
        for i in took_my_coords:
            col = i[1]
            col = int(col)
            cool_cols.append(col)
        cool_cols.sort()
        # cur_col = random.choice(cool_cols)
        # cur_col = int(cur_col)
        # cool_cols.remove(cur_col)
        return cool_cols


    def shoot(self, row: int, col: int) -> bool:
        # this is checking the board of the player who's being shot at (ie not the player in the current turn)

        # check if the coordinates contains a ship,
        # and return False if there is no ship
        # if there is a ship,
        # look up which ship the initials correspond to, mark an X, and return True
        if self.board.contents[1][row][col] == '*':
            self.board.contents[1][row][col] = 'O'
            return False
        else:
            ship_initial = self.board.contents[1][row][col]
            for ship in self.ship_list:
                if ship.name[0] == ship_initial:
                    self.board.contents[1][row][col] = 'X'
                    ship.got_hit(self.name)
                    return True

    def turn(self, other_player):
        self.get_player_board()

        stole_their_coords = self.ship_coords
        cur_coords = random.choice(stole_their_coords)
        self.ship_coords.remove(cur_coords)

        row = cur_coords[0]
        col = cur_coords[1]

        # print(row, col)


        # im being dumb and the row and col values get duplicated if i separate them lmao
        # dumb = self.row_list
        # ugh = self.col_list
        # row = random.choice(dumb)
        # col = random.choice(ugh)
        # print(row, col)
        #
        # dumb.remove(row)
        # ugh.remove(col)

        hit = other_player.shoot(row, col)

        # mark scanning boards accordingly
        if hit:
            self.board.contents[0][row][col] = 'X'
        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()

    def __str__(self) -> str:
        # convert player name from weird object thing to str
        return self.name
