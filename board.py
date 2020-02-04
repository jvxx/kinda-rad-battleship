import typing
from typing import Iterator, List, Callable
from ship import Ship
import sys


class Board(object):

    def __init__(self, rows: int, cols: int, blank_char: str) -> None:
        self.blank_char = blank_char
        self.contents = [[blank_char for col in range(rows)] for row in range(cols)]
        #self.blank_char = blank_char

    @property
    def rows(self) -> int:
        return len(self.contents)

    @property
    def cols(self) -> int:
        return len(self[0])

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.rows)), len(str(self.cols))])

        rep = sep * 2 + sep.join((str(i) for i in range(self.cols))) + '\n'

        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.rows and
                0 <= col < self.cols)


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

    def place_the_damn_ship(self, row, col):
        if not self.is_in_bounds(row, col):
            print(f'{row}, {col} is not in bounds')
        else:
            print('no')


'''
MY COOL GRID THAT CANNOT BE USED :(
    
    self.rows = rows
    self.cols = cols
    
    def _create_empty_contents(self, blank_char):
        empty_contents = []
        for row in range(self.rows):
            row = []
            for col in range(self.cols):
                row.append(blank_char)
            empty_contents.append(row)
        return empty_contents
        
    def display_board(self):
        # board = self._create_empty_contents()
        board = self.contents
        cols = self.cols + 1

        c_list = []
        for c in range(cols+1):
            c = str(c)
            c_list.append(c)
        nums = ''.join(c_list)

        row_name = nums[:cols]
        print('  ' + ' '.join(row_name) + '')
        for num, row in enumerate(board):
            print(num, '*', ' '.join(row[1:]))
'''
