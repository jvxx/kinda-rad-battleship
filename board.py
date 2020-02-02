import typing
from typing import Iterator, List, Callable
from ship import Ship
import sys

class Board(object):

    def __init__(self, rows, cols):
        self.rows = int(rows)
        self.cols = int(cols)
        #self.ships = shipList
        ...

    def create_board(self):
        board = []
        for row in range(self.rows + 1):
            row = []
            for col in range(self.cols + 1):
                row.append('*')
            board.append(row)
        return board


    def display_board(self):
        board = self.create_board()
        cols = self.cols + 1
        row_name = '01234567891011'[:cols]
        print('  ' + ' '.join(row_name) + '')
        for num, row in enumerate(board):
            print(num, '*', ' '.join(row[1:]))



    def place_ship(self):
        if self.place_ship_orient() == 'horizontal':
            pass
        elif self.place_ship_orient() == 'vertical':
            pass
        # alright get all these answers
        # validate
        # place ship
        # exit loop
        ...

    @staticmethod
    def place_ship_orient(self) -> str:
        # ship orientation: horizontal or vertical
        while True:
            ship_orientation = input(
                f'{self} how do you want your ship: vertical or horizontal?: '
            )
            if ship_orientation in "horizontal":
                return ship_orientation

            elif ship_orientation in "vertical":
                return ship_orientation

            else:
                print(
                    f'{ship_orientation} is not horizontal or vertical, bro'
                )


    @staticmethod
    def place_ship_location(self):
        # ship location: x, y coordinates
        while True:
            ship_location = input(
                f'{self} where do you want your ship in row, col?: '
            )
            try:
                row, col = ship_location.split(',')
            except ValueError:
                raise UhOh(
                    f"{ship_location} is not in the right format 'row, col'"
                )
            try:
                row = int(row)
            except ValueError:
                raise UhOh(
                    f'{row} is not an integer'
                )
            try:
                col = int(col)
            except ValueError:
                raise UhOh(
                    f'{col} is not an integer'
                )
            return row, col

        ...

    def shoot(self):
        # prompt
        # validate
        # board look up
            # board look up if * X O then miss
            # else ship look up
            # ship..hit
            # place X
            # check win
        ...

    def check_any_wins(self):
        # if ship hp = 0
        # then print ship sank
        # and remove ship from list
        # if board.ship.size is 0 then u lose
        ...


if __name__ == '__main__':
    test = Board(5,5)

    print(test.display_board())


    test.place_ship_orient('nes')

'''
while True:
    ship_orientation = input(
        f'how do you want your ship: vertical or horizontal?: '
    ).strip()

    if ship_orientation not in ['horizontal', 'vertical']:
        print('bruh')
    else:
        print('nice')
    '''
