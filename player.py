import sys
from typing import Iterable, Iterator
from board import Board
from move import Move
from ship import Ship

class Player(object):
    def __init__(self, other_players: Iterable["Player"], row, col, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        self.blank_char = blank_char
        self.board = Board(row, col, blank_char)
        self.name = self.get_player_name(other_players)
        self.ship_list = self.get_player_ship()

        # this returns our Move object
        self.ship_placement = self.get_ship_placement()
        ...

    @staticmethod
    def get_player_name(other_players: Iterable['Player']) -> str:
        taken_names = set([player.name for player in other_players])
        while True:
            name = input("What's your name?: ")
            if name not in taken_names:
                return name
            else:
                print(f'{name} is taken. You should choose a more original name.')


    def get_player_ship(self):
        ship_list = []
        with open(sys.argv[1]) as fil:
            #all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]

            for s in fil.readlines()[1:]:
                s = s.split(' ')
                ship_name = s[0]
                ship_length = int(s[1])
                ship_list.append(Ship(ship_name, ship_length))

            #ship_names, ship_lengths = zip(*all_these_ships)

            return ship_list

    def get_ship_orient(self, ship) -> bool:
        # ship orientation: horizontal or vertical
        while True:
            ship_orientation = input(
                f'{self} how do you want your {ship.name} ship: vertical or horizontal?: '
            )
            if ship_orientation in "horizontal":
                return True

            elif ship_orientation in "vertical":
                return False

            else:
                print(
                    f'{ship_orientation} is not horizontal or vertical, bro'
                )



    def get_ship_placement(self):
        self.get_player_board()
        for ship in self.ship_list:
            valid_input = 0
            # horz or vert
            is_horiz = self.get_ship_orient(ship)

            while valid_input < 3:
                place_ship = input(f'{self} where do you want to place your {ship.name} ship in row, col?: ')
                valid_input = 0
                try:
                    row, col = place_ship.split(',')
                    valid_input += 1
                except:
                    print(f'{place_ship} is not in the form row, col')
                    continue

                try:
                    row = int(row)
                    valid_input += 1
                except:
                    print(f'row needs to be an integer. that is not an integer')
                    continue

                try:
                    col = int(col)
                    valid_input += 1
                except:
                    print(f'col needs to be an integer. that is not an integer')
                    continue

                fake_col = col
                fake_row = row
                for ship_length in range(ship.length):
                    if not self.board.is_in_bounds(fake_row, fake_col):
                        valid_input = 0
                        print(f'{fake_row}, {fake_col} is not in bounds')
                        break

                    elif self.board.contents[0][fake_row][fake_col] != '*':
                        valid_input = 0
                        print(f"you can't play at {row}, {col} because u already played there")
                        break

                    if is_horiz is True:
                        fake_col += 1
                    else:
                        fake_row += 1

            for ship_length in range(ship.length):
                self.board.contents[0][row][col] = ship.name[0]
                if is_horiz is True:
                    col += 1
                else:
                    row += 1

            self.get_player_board()



    def shoot(self, row, col) -> bool:
        if self.board.contents[0][row][col] == '*':
            self.board.contents[0][row][col] = 'O'
            return False
        elif self.board.contents[0][row][col] == 'X':
            return False
        elif self.board.contents[0][row][col] == 'O':
            return False
        else:
            ship_initial = self.board.contents[0][row][col]
            for ship in self.ship_list:
                if ship.name[0] == ship_initial:
                    self.board.contents[0][row][col] = 'X'
                    ship.got_hit()
                    return True



    def __str__(self) -> str:
        # convert player name from generator -> str
        return self.name


    def get_player_board(self):
        print(" ",end='')
        for i in range(2):
            for col_num in range(self.col):
                print(" " + str(col_num), end = '')
            print()
            for row_num in range(self.row):
                print(row_num, end = '')
                for col_num in range(self.col):
                    print(" " + self.board.contents[i][row_num][col_num], end = '')
                print()

        ...


    def turn(self, other_player):
        self.get_player_board()
        valid_input = 0
        while valid_input < 3:
            valid_input = 0
            shoot_me = input(f'{self} where u wanna shoot pls enter in row, col: ')

            try:
                row, col = shoot_me.split(',')
                valid_input += 1
            except:
                print(f'cmon man {shoot_me} is not in the form row, col')
                continue

            try:
                row = int(row)
                valid_input += 1
            except:
                print(f'row needs to be an integer. that is not an integer')
                continue

            try:
                col = int(col)
                valid_input += 1
            except:
                print(f'col needs to be an integer. that is not an integer')
                continue
            #
            # for ship in self.ship_list:
            #     for ship_length in range(ship.length):
            if not self.board.is_in_bounds(row, col):
                valid_input = 0
                print(f'{row}, {col} is not in bounds')
                continue


        hit = other_player.shoot(row, col)

        if hit:
            self.board.contents[1][row][col] = 'X'
        else:
            self.board.contents[1][row][col] = 'O'
        ...



