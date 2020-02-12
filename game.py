from humanplayer import HumanPlayer


class Game(object):

    def __init__(self, row, col, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        # self.player_board = Player.get_player_board(self)
        self.players = []
        for player_num in range(1, 3):
            self.players.append(HumanPlayer(self.players, row, col, player_num, blank_char))
        self._cur_player_turn = 0

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    @property
    def cur_player(self) -> "HumanPlayer":
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
