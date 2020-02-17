import random
from typing import Iterable
from player import Player
from aiplayer import AIPlayer


# command line args: configs/minor_game.txt 542

class SearchDestroyAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)
        self.hit_coords = []

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Search Destroy AI {playerNum}"
        return name

    def get_player_ship(self):
        return super().get_player_ship()

    def initial_player_board(self):
        super().initial_player_board()

    def get_player_board(self):
        super().get_player_board()

    def get_ship_placement(self):
        self.initial_player_board()
        super().get_ship_placement()

    def stealin_my_coords(self):
        return super().stealin_my_coords()

    def random_coords(self):
        return super().random_coords()

    def shoot(self, row: int, col: int) -> bool:
        return super().shoot(row, col)

    def turn(self, other_player):
        """
        search:
        shooting at random coordinates like random ai,
        but once we hit -- enter DESTROY mode

        destroy:
        generate a list of coordinates to the left, top, right, and bottom respectively.
        go through all the coordinates of the list before returning to search mode.

        this addition of coordinates to the list is repeated with each hit

        of course, the coordinates have to be valid:
        (not already in the list, not out of bounds, not already hit)
        """
        stole_their_coords = other_player.random_coords
        self.get_player_board()
        if self.hit_coords:
            cur_coords = self.hit_coords.pop(0)
            row = cur_coords[0]
            col = cur_coords[1]

            stole_their_coords.remove(cur_coords)

        else:
            cur_coords = random.choice(stole_their_coords)
            stole_their_coords.remove(cur_coords)

            row = cur_coords[0]
            col = cur_coords[1]

        hit = other_player.shoot(row, col)

        if hit:
            self.board.contents[0][row][col] = 'X'

            if self.board.is_in_bounds(row, col - 1) and self.board.contents[0][row][col - 1] == '*':
                left_coords = (row, col - 1)
                if left_coords not in self.hit_coords:
                    self.hit_coords.append(left_coords)
            if self.board.is_in_bounds(row - 1, col) and self.board.contents[0][row - 1][col] == '*':
                top_coords = (row - 1, col)
                if top_coords not in self.hit_coords:
                    self.hit_coords.append(top_coords)
            if self.board.is_in_bounds(row, col + 1) and self.board.contents[0][row][col + 1] == '*':
                right_coords = (row, col + 1)
                if right_coords not in self.hit_coords:
                    self.hit_coords.append(right_coords)
            if self.board.is_in_bounds(row + 1, col) and self.board.contents[0][row + 1][col] == '*':
                bottom_coords = (row + 1, col)
                if bottom_coords not in self.hit_coords:
                    self.hit_coords.append(bottom_coords)

        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()

    def __str__(self) -> str:
        return super().__str__()
