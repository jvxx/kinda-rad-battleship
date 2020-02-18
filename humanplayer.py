from typing import Iterable, List
from player import Player


class HumanPlayer(Player):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        """
        take their name and player number--
        asking for someone's number is just this easy!
        """
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
        return super().get_player_ship()

    def get_ship_orient(self, ship) -> str:
        """
        ask how they'd like their ship to be oriented.
        check if it's a valid input and orientation.
        """
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
        super().initial_player_board()

    def get_player_board(self):
        super().get_player_board()

    def get_ship_placement(self):
        """
        iterating through list of ships and placing them down

        unfortunately, unlike AI, humans are imperfect and we'll need to check if:
        a) their coordinates are in the right format so we can parse it
        b) if every coordinate the ship will be on is valid
        """

        self.initial_player_board()

        """
        iterate through ship list and place each ship
        """
        for ship in self.ship_list:
            valid_input = 0

            """
            valid_input counter with while loop to track if each requirement is met
            """
            while valid_input < 3:
                is_horiz = self.get_ship_orient(ship)
                place_ship = input(
                    f'{self}, enter the starting position for your {ship.name} ship ,which is {ship.length} long, in the form row, column: '
                )

                valid_input = 0

                """
                a) determine if user input of coordinates is the correct format
                """
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

                """
                b) to check if each and every coordinate the ship will be on is valid
                """
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

                    """
                    incrementing by 1 to check every coordinate the ship will be on;
                    we'll go through all the coordinates the ship will be on
                    """
                    if is_horiz == 'horizontal':
                        fake_col += 1
                    elif is_horiz == 'vertical':
                        fake_row += 1

            """
            once all the coordinates and placements are confirmed to be valid,
            place the ship's initials to mark the ship on the board
            """
            for ship_length in range(ship.length):
                self.board.contents[1][row][col] = ship.name[0]
                if is_horiz == 'horizontal':
                    col += 1
                elif is_horiz == 'vertical':
                    row += 1

            self.initial_player_board()

    def stealin_my_coords(self):
        return super().stealin_my_coords()

    def random_coords(self):
        return super().random_coords()

    def shoot(self, row: int, col: int) -> bool:
        return super().shoot(row, col)

    def turn(self, other_player):
        self.get_player_board()
        valid_input = 0
        while valid_input < 3:
            valid_input = 0
            shoot_me = input(f'{self}, enter the location you want to fire at in the form row, column: ')

            """
            check if input of shooting coordinates is correct format
            """
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

            """
            check validity of coordinates
            """
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

        """
        now shoot at the other player
        """
        hit = other_player.shoot(row, col)

        """
        mark scanning boards accordingly if everything goes well
        """
        if hit:
            self.board.contents[0][row][col] = 'X'
        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()

    def __str__(self) -> str:
        return super().__str__()
