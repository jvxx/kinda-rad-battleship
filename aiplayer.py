import random
import sys
from typing import Iterable
from BattleShip.src import orientation
from ship import Ship
from player import Player
import abc
from copy import deepcopy

# random.seed(sys.argv[2])

class AIPlayer(Player):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)
        self.ship_coords = self.stealin_my_coords
        self.row_list = self.stolen_rows()
        self.col_list = self.stolen_cols()

    @abc.abstractmethod
    def stealin_my_coords(self):
        ...

    @abc.abstractmethod
    def stolen_rows(self):
        ...

    @abc.abstractmethod
    def stolen_cols(self):
        ...

    def place_ship(self, ship: "Ship") -> None:
        while True:
            placement = self.get_ship_placement(ship)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return

    # def get_ship_orient(self, ship) -> str:
    #     # is_horiz = random.randint(0, 1)
    #     # if is_horiz == 0:
    #     #     return True
    #     # else:
    #     #     return False
    #     orient_list = ['horizontal', 'vertical']
    #     f = random.choice(orient_list)
    #     return deepcopy(f)

    def get_ship_placement(self):
        orient_list = ['horizontal', 'vertical']

        # iterate through ship list and place each ship
        for ship in self.ship_list:
            valid_input = 0
            while valid_input < 2:
                # retrieve orientation of the ship
                is_horiz = random.choice(orient_list)

                if is_horiz == 'horizontal':
                    row = random.randint(0, self.board.rows - 1)
                    col = random.randint(0, self.board.cols - ship.length)
                    valid_input += 1

                elif is_horiz == 'vertical':
                    row = random.randint(0, self.board.rows - ship.length)
                    col = random.randint(0, self.board.cols - 1)
                    valid_input += 1

                # to check if each and every coordinate the ship will be on is valid
                fake_col = col
                fake_row = row
                for ship_length in range(ship.length):
                    if not self.board.is_in_bounds(fake_row, fake_col):
                        valid_input = 0
                        break

                    elif self.board.contents[1][fake_row][fake_col] != '*':
                        valid_input = 0
                        break

                    elif is_horiz == 'horizontal':
                        if col + ship.length > self.board.cols:
                            valid_input = 0
                            break

                    elif is_horiz == 'vertical':
                        if row + ship.length > self.board.rows:
                            valid_input = 0
                            break

                    # incrementing by 1 to check every coordinate the ship will be on
                    if is_horiz == 'horizontal':
                        fake_col += 1
                    elif is_horiz == 'vertical':
                        fake_row += 1

            # once all the coordinates and placements are confirmed to be valid,
            # place the ship's initials to mark the ship on the board
            for ship_length in range(ship.length):
                self.board.contents[1][row][col] = ship.name[0]
                if is_horiz == 'horizontal':
                    col += 1
                elif is_horiz == 'vertical':
                    row += 1





        '''
        works - but will overlap :(
        for ship in self.ship_list:
            # is_horiz = self.get_ship_orient(ship)
            is_horiz = 'horizontal' # test for current bc that's returning None. ...

            # for ship_length in range(ship.length):
            if is_horiz == 'horizontal':
                row = random.randint(0, self.board.rows - 1)
                col = random.randint(0, self.board.cols - ship.length)
                for ship_length in range(ship.length):
                    if self.board.contents[1][row][col] != '*':
                        pass
                        # would overlap with self.board.contents[1][row][col]
                    self.board.contents[1][row][col] = ship.name[0]
                    col += 1

            elif is_horiz == 'vertical':
                for ship_length in range(ship.length):
                    row = random.randint(0, self.board.rows - ship.length)
                    col = random.randint(0, self.board.cols - 1)
                    self.board.contents[1][row][col] = ship.name[0]
                    row += 1
        '''

        # original starter code from butner
        #
        # if orientation_ == orientation.Orientation.HORIZONTAL:
        #     row = random.randint(0, self.board.rows - 1)
        #     col = random.randint(0, self.board.cols - ship.length)
        # else:
        #     row = random.randint(0, self.board.rows - ship.length)
        #     col = random.randint(0, self.board.cols - 1)
        # return row, col