import random
from typing import Iterable
from player import Player


class AIPlayer(Player):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)

    def get_ship_placement(self):
        """
        each ship is placed randomly:
        random orientation is chosen, and
        random coordinates are chosen and checked for validity.
        if bad, choose random coordinates again and again and again till good
        """
        orient_list = ['horizontal', 'vertical']

        for ship in self.ship_list:
            valid_input = 0
            while valid_input < 2:
                is_horiz = random.choice(orient_list)

                if is_horiz == 'horizontal':
                    row = random.randint(0, self.board.rows - 1)
                    col = random.randint(0, self.board.cols - ship.length)
                    valid_input += 1

                elif is_horiz == 'vertical':
                    row = random.randint(0, self.board.rows - ship.length)
                    col = random.randint(0, self.board.cols - 1)
                    valid_input += 1

                """
                to check if each and every coordinate the ship will be on is valid
                """
                fake_col = col
                fake_row = row
                for ship_length in range(ship.length):
                    if not self.board.is_in_bounds(fake_row, fake_col):
                        valid_input = 0
                        break

                    elif self.board.contents[1][fake_row][fake_col] != '*':
                        valid_input = 0
                        break

                    """
                    incrementing by 1 to check every coordinate the ship will be on
                    """
                    if is_horiz == 'horizontal':
                        fake_col += 1
                    elif is_horiz == 'vertical':
                        fake_row += 1
                valid_input += 1

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


