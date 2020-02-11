import sys
from typing import Iterable
from board import Board
from ship import Ship

#bobalicious
class Player(object):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        self.blank_char = blank_char
        self.board = Board(row, col, blank_char)
        self.name = self.get_player_name(player_num, other_players)
        self.ship_list = self.get_player_ship()
        self.ship_placement = self.get_ship_placement()

    @staticmethod
    def get_player_name(playerNum: int, other_players: Iterable['Player']) -> str:
        taken_names = set([player.name for player in other_players])
        while True:
            name = input(
                f"Player {playerNum} please enter your name: "
            )
            if name not in taken_names:
                return name
            else:
                print(
                    f'Someone is already using {name} for their name.\nPlease choose another name.'
                )

    def get_player_ship(self):
        ship_list = []
        with open(sys.argv[1]) as fil:
            for s in fil.readlines()[1:]:
                s = s.split(' ')
                ship_name = s[0]
                ship_length = int(s[1])
                ship_list.append(Ship(ship_name, ship_length))

            return ship_list

    def get_ship_orient(self, ship) -> str:
        # ship orientation: horizontal or vertical
        while True:
            ship_orientation = input(
                f'{self} enter horizontal or vertical for the orientation of {ship.name} which is {ship.length} long: '
            )
            ship_orientation = ship_orientation.lower()
            ship_orientation = ship_orientation.strip()

            if 'horizontal'.startswith(ship_orientation):
                ship_orientation = 'horizontal'
                return ship_orientation

            elif 'vertical'.startswith(ship_orientation):
                ship_orientation = 'vertical'
                return ship_orientation

            else:
                print(
                    f'{ship_orientation} does not represent an Orientation'
                )

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
        # WE NEED THE PLACEMENT BOARD HERE
        self.initial_player_board()

        # iterate through ship list and place each ship
        for ship in self.ship_list:
            valid_input = 0
            while valid_input < 3:

                # retrieve orientation of the ship
                is_horiz = self.get_ship_orient(ship)
                place_ship = input(
                    f'{self}, enter the starting position for your {ship.name} ship ,which is {ship.length} long, in the form row, column: '
                )

                # to track if each requirement is met for a valid input
                valid_input = 0

                # determine validity of user input of coordinates
                try:
                    row, col = place_ship.split(',')
                    valid_input += 1
                except:
                    if place_ship.isalpha() and len(place_ship) == 1:
                        continue
                    else:
                        print(
                            f'{place_ship} is not in the form x,y'
                        )
                        continue
                try:
                    row = int(row)
                    valid_input += 1
                except:
                    print(
                        f'{row} is not a valid value for row.\nIt should be an integer between 0 and {self.board.rows - 1}'
                    )
                    continue

                try:
                    col = int(col)
                    valid_input += 1
                except:
                    print(
                        f'{col} is not a valid value for column.\nIt should be an integer between 0 and {self.board.cols - 1}'
                    )
                    continue

                # to check if each and every coordinate the ship will be on is valid
                fake_col = col
                fake_row = row
                for ship_length in range(ship.length):
                    if not self.board.is_in_bounds(fake_row, fake_col):
                        valid_input = 0
                        print(
                            f'Cannot place {ship.name} {is_horiz}ly at {row}, {col} because it would be out of bounds.'
                        )
                        break

                    elif self.board.contents[1][fake_row][fake_col] != '*':
                        valid_input = 0
                        print(
                            f"Cannot place {ship.name} {is_horiz}ly at {row}, {col} because it would overlap with ['{self.board.contents[1][fake_row][fake_col]}']"
                        )
                        break

                    elif is_horiz == 'horizontal':
                        if col + ship.length > self.board.cols:
                            valid_input = 0
                            print(
                                f'Cannot place {ship.name} {is_horiz}ly at {row}, {col} because it would end up out of bounds.'
                            )
                            break


                    elif is_horiz == 'vertical':
                        if row + ship.length > self.board.rows:
                            valid_input = 0
                            print(
                                f'Cannot place {ship.name} {is_horiz}ly at {row}, {col} because it would end up out of bounds.'
                            )
                            break

                    # if is_horiz is True:
                    #     fake_col += 1
                    # else:
                    #     fake_row += 1
                    # else:

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

            self.initial_player_board()

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

    def turn(self, other_player):
        self.get_player_board()
        valid_input = 0
        while valid_input < 3:
            valid_input = 0
            shoot_me = input(f'{self}, enter the location you want to fire at in the form row, column: ')

            # check validity of shooting coordinates format
            try:
                row, col = shoot_me.split(',')
                valid_input += 1
            except:
                print(
                    f'{shoot_me} is not a valid location.\nEnter the firing location in the form row, column'
                )
                continue

            try:
                row = int(row)
                valid_input += 1
            except:
                print(
                    f'Row should be an integer. {row} is NOT an integer.'
                )
                continue

            try:
                col = int(col)
                valid_input += 1
            except:
                print(
                    f'Column should be an integer. {col} is NOT an integer.'
                )
                continue

            # check validity of coordinates
            if not self.board.is_in_bounds(row, col):
                valid_input = 0
                print(
                    f'{row}, {col} is not in bounds of our {self.board.rows} X {self.board.cols} board.'
                )
                continue
            elif self.board.contents[0][row][col] == 'X':
                valid_input = 0
                print(
                    f'You have already fired at {row}, {col}.'
                )
            elif self.board.contents[0][row][col] == 'O':
                valid_input = 0
                print(
                    f'You have already fired at {row}, {col}.'
                )

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
