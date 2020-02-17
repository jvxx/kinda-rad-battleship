import random
from typing import Iterable
from player import Player
from aiplayer import AIPlayer


# command line args: configs/minor_game.txt 89

class RandomAI(AIPlayer):
    def __init__(self, other_players: Iterable["Player"], row, col, player_num: int, blank_char: str = '*') -> None:
        super().__init__(other_players, row, col, player_num, blank_char)

    def get_player_name(self, playerNum: int, other_players: Iterable['Player']) -> str:
        name = f"Random Ai {playerNum}"
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
        just shootin' at random coordinates
        may the force be with me :(
        """
        self.get_player_board()

        stole_their_coords = other_player.random_coords
        cur_coords = random.choice(stole_their_coords)
        stole_their_coords.remove(cur_coords)

        row = cur_coords[0]
        col = cur_coords[1]

        hit = other_player.shoot(row, col)

        if hit:
            self.board.contents[0][row][col] = 'X'
        else:
            self.board.contents[0][row][col] = 'O'
            print('Miss')

        self.get_player_board()

    def __str__(self) -> str:
        return super().__str__()
