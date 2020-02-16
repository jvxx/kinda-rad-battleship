import random
from player import Player
from humanplayer import HumanPlayer
from aiplayer import AIPlayer
from cheatingai import CheatingAI
from randomai import RandomAI
from searchdestroyai import SearchDestroyAI


class Game(object):

    def __init__(self, row, col, random_seed, blank_char: str = '*') -> None:
        random.seed(random_seed)
        self.row = row
        self.col = col
        # self.player_board = Player.get_player_board(self)
        self.players = []
        for player_num in range(1, 3):
            self.players.append(self.get_player_type(self.players, row, col, player_num, blank_char))
            # self.which_player = Player.get_player_type(player_num)
        self._cur_player_turn = 0

    def get_player_type(self, otherPlayers, row, col, playerNum: int, blank_char):
        while True:
            who_are_you = input(
                f"Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {playerNum}'s type: "
            )
            who_are_you = who_are_you.lower()
            who_are_you = who_are_you.strip()
            if 'human'.startswith(who_are_you):
                return HumanPlayer(otherPlayers, row, col, playerNum, blank_char)
            elif 'cheatingai'.startswith(who_are_you):
                return CheatingAI(otherPlayers, row, col, playerNum, blank_char)
            elif 'searchdestroyai'.startswith(who_are_you):
                return SearchDestroyAI(otherPlayers, row, col, playerNum, blank_char)
            elif 'randomai'.startswith(who_are_you):
                return RandomAI(otherPlayers, row, col, playerNum, blank_char)
            else:
                continue

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    @property
    def cur_player(self) -> get_player_type:
        return self.players[self._cur_player_turn]


    def play(self):
        while not self.game_over():
            self.cur_player.turn(self.players[(self._cur_player_turn + 1) % 2])
            self.change_turn()
        self.change_turn()
        print(
            f'{self.cur_player.name} won the game!'
        )

    def game_over(self):
        for ship in self.cur_player.ship_list:
            if ship.length != 0:
                return False
        return True
