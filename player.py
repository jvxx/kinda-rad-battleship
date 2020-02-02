import sys
from typing import Iterable
from board import Board

class Player(object):
    def __init__(self, x: int, y:int):
        self.name = self.get_player_name(other_players)
        self.place_ship = Board.placeship()
        self.board = Board(x, y)
        self.shoot = Board(x, y)
        self.did_i_win = Board()
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


    @staticmethod
    def get_player_ship(ships):
        for ship in ships:
            Board.place_ship()

    def turn(self):
        #print(self.board)
        #self.shoot
        #self.did_i_win
        ...


    def whats_the_move(self):
        while True:
            where_to_shoot = input(
                "where we droppin' bois? enter in row, col format: "
            )
        ...


    '''
    def __init__(self, other_players: Iterable['Player'], blank_character: str) -> None:
        self.name = self.get_player_name(other_players)
        self.ship = self.get_player_ship(other_players, blank_character)
        self.ShipPlacement = Ship_Placement(coordinates, coordinates)

    @staticmethod
    def get_player_name(other_players: Iterable['Player']) -> str:
        # sets have v fast operating times! O(1)!!
        taken_names = set([player.name for player in other_players])
        while True:
            name = input("What's your name?: ")
            if name not in taken_names:
                return name
            else:
                print(f'{name} is taken. You should choose a more original name.')

    @staticmethod
    def get_player_ship(other_players: Iterable["Player"], blank_character: str) -> str:
        already_used_ships = set([player.ship for player in other_players])
        while True:
            ship = input()

        ##
        lmao idk fam
        while True:
            ship = input('Please enter the piece you want use: ').strip()
            if len(ship) > 1:
                print("You piece may only be a single character. Pick another piece.")
            elif ship == blank_character:
                print(f'You cannot pick {blank_character} for your piece. Pick another piece.')
            elif ship in already_used_ships:
                print(f'{ship} has already been used. Pick another piece.')
            else:
                return ship
        ##


    def __str__(self) -> str:
        return self.name

    def take_turn(self) -> None:
        while True:
            try:
                move = self.get_move()
                move.do()
            except MoveError:
                print(MoveError)

    def get_player_move(self, x: int, y: int) -> 'Move':
        str_move = input(f'{self} Enter where you want to play in x, y coordinates: ')
        return Move.from_str(self, str_move)
        # keep asking for their moves IF they keep making wrong moves
        #try:
            #return Move.from_str(self, str_move)
        #except MoveError:
            #print(MoveError)

    '''