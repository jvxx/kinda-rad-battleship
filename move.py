import humanplayer
import board
from ship import Ship



class Move(object):
    def __init__(self, maker: "humanplayer.Player", row: int, col: int, name: str, length: int) -> None:
        self.maker = maker
        self.row = row
        self.col = col
        self.ship = Ship(name, length)

    def check_ship(self, row, col):
        ship_orient = self.place_ship_orient()
        ship_length = Ship.ship_size()
        board_width = self.row
        board_length = self.col

        if ship_orient == 'horizontal':
            if row + ship_length > board_width:
                for i in range(ship_length):
                    if [row+i, col] != '*':
                        print('BAD!')
                    else:
                        print('nice')

        elif ship_orient == 'vertical':
            if col + ship_length > board_length:
                for i in range(ship_length):
                    if [row, col+i] != '*':
                        print('STOP THAT!')
                    else:
                        print('nice')
        # loop until we get a nice answer
        # place ship
        # exit loop
    def place_ship(self):
        ...



    @classmethod
    def from_str(cls, maker: "humanplayer.Player", place_ship_inp: str, name_list: list, length_list: list) -> "Move":

        return cls(maker, row, col, name, length)




    def make(self, the_board: "board.Board"):
        print('hey you made it')
        print(self.row, self.col)

        if not the_board.is_in_bounds(self.row, self.col):
            print(f'{self.row}, {self.col} is not in bounds')

        elif the_board[self.row][self.col] != '*':
            print(f"You can't play at {self.row}, {self.col} because someone already played there")

        else:
            the_board[self.row][self.col] = self.maker.ship_list
