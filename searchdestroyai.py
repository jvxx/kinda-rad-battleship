import sys
import random
from typing import Iterable
from ship import Ship
from player import Player
from aiplayer import AIPlayer
from BattleShip.src import orientation

# command line args: configs/minor_game.txt 542

class SearchDestroyAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)
        self.row_hitList = []
        self.col_hitList = []
        self.hit_this = []
        self.hit_coords = []

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Search Destroy AI {playerNum}"
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
            # row = int(row)
            rad_rows.append(row)
        rad_rows.sort()
        # cur_row = random.choice(rad_rows)
        # cur_row = int(cur_row)
        # rad_rows.remove(cur_row)
        # return cur_row
        return rad_rows

    def stolen_cols(self):
        took_my_coords = self.stealin_my_coords()
        cool_cols = []
        for i in took_my_coords:
            col = i[1]
            # col = int(col)
            cool_cols.append(col)
        cool_cols.sort()
        # cur_col = random.choice(cool_cols)
        # cur_col = int(cur_col)
        # cool_cols.remove(cur_col)
        # return cur_col
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

    '''
    senf help thank
    def hit_list(self, row, col):
        row_hitList = []
        col_hitList = []

        if self.board.is_in_bounds(row, col - 1): #and row in self.row_list and (col - 1) in self.col_list:
            self.row_hitList.append(row)
            self.col_hitList.append(col - 1)
        if self.board.is_in_bounds(row - 1, col): #and (row - 1) in self.row_list and col in self.col_list:
            self.row_hitList.append(row - 1)
            self.col_hitList.append(col)
        if self.board.is_in_bounds(row, col + 1): #and row in self.row_list and (col + 1) in self.col_list:
            self.row_hitList.append(row)
            self.col_hitList.append(col + 1)
        if self.board.is_in_bounds(row + 1, col): #and (row + 1) in self.row_list and col in self.col_list:
            self.row_hitList.append(row + 1)
            self.col_hitList.append(col)
        hit_coords = list(zip(self.row_hitList, self.col_hitList))
        # print(hit_coords)
        return hit_coords
    '''

    def turn(self, other_player):
        # row_hitList = self.row_hitList
        # col_hitList = self.col_hitList
        # hit_coords = self.hit_this
        stole_their_coords = self.ship_coords
        self.get_player_board()
        if self.hit_coords:
            # return and remove first row element from list
            cur_coords = self.hit_coords.pop(0)
            row = cur_coords[0]
            col = cur_coords[1]
            # print(row, col)
            # row = int(cur_row)
            # remove said row element from original list of coords
            # self.row_list.remove(cur_row)

            # return and remove first col element from list
            # cur_col = self.hit_this.pop(0)
            # col = int(cur_col)
            # remove same col element from og list of coords
            # self.col_list.remove(cur_col)

            self.ship_coords.remove(cur_coords)
            # print(self.hit_coords)

        else:
            # stole_their_coords = self.ship_coords
            cur_coords = random.choice(stole_their_coords)
            self.ship_coords.remove(cur_coords)

            row = cur_coords[0]
            col = cur_coords[1]
            # print(row, col)



        hit = other_player.shoot(row, col)

        if hit:
            #  mark scanning boards accordingly
            self.board.contents[0][row][col] = 'X'

            if self.board.is_in_bounds(row, col - 1) and self.board.contents[0][row][col - 1] == '*':  # and row in self.row_list and (col - 1) in self.col_list:
                left_coords = (row, col - 1)
                if left_coords not in self.hit_coords:
                    self.hit_coords.append(left_coords)
                # self.row_hitList.append(row)
                # self.col_hitList.append(col - 1)
            if self.board.is_in_bounds(row - 1, col) and self.board.contents[0][row - 1][col] == '*':  # and (row - 1) in self.row_list and col in self.col_list:
                top_coords = (row - 1, col)
                if top_coords not in self.hit_coords:
                    self.hit_coords.append(top_coords)
                # self.row_hitList.append(row - 1)
                # self.col_hitList.append(col)
            if self.board.is_in_bounds(row, col + 1) and self.board.contents[0][row][col + 1] == '*':  # and row in self.row_list and (col + 1) in self.col_list:
                right_coords = (row, col + 1)
                if right_coords not in self.hit_coords:
                    self.hit_coords.append(right_coords)
                # self.row_hitList.append(row)
                # self.col_hitList.append(col + 1)
            if self.board.is_in_bounds(row + 1, col) and self.board.contents[0][row + 1][col] == '*':  # and (row + 1) in self.row_list and col in self.col_list:
                bottom_coords = (row + 1, col)
                if bottom_coords not in self.hit_coords:
                    self.hit_coords.append(bottom_coords)
                # self.row_hitList.append(row + 1)
                # self.col_hitList.append(col)
            # print(self.hit_coords)



            # dude = self.hit_list(row, col)
            # print(dude)


            # check if in bounds and add coords to hit list
            # if self.board.is_in_bounds(row, col - 1) and row in self.row_list and (col - 1) in self.col_list:
            #     row_hitList.append(row)
            #     col_hitList.append(col-1)
            # if self.board.is_in_bounds(row - 1, col) and (row - 1) in self.row_list and col in self.col_list:
            #     row_hitList.append(row-1)
            #     col_hitList.append(col)
            # if self.board.is_in_bounds(row, col + 1) and row in self.row_list and (col + 1) in self.col_list:
            #     row_hitList.append(row)
            #     col_hitList.append(col + 1)
            # if self.board.is_in_bounds(row + 1, col) and (row + 1) in self.row_list and col in self.col_list:
            #     row_hitList.append(row+1)
            #     col_hitList.append(col)
        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()


    def __str__(self) -> str:
        # convert player name from weird object thing to str
        return self.name
