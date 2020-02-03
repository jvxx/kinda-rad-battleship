import sys
from typing import Iterable
from board import Board
from move import Move
from ship import Ship


class MoveError(Exception):
    ...


class Player(object):
    def __init__(self, other_players: Iterable["Player"]) -> None:
        self.name = self.get_player_name(other_players)
        self.ship = self.get_player_ship()
        self.make = Move
        ...

    def get_player_name(self, other_players: Iterable['Player']) -> str:
        taken_names = set([player.name for player in other_players])
        while True:
            name = input("What's your name?: ")
            if name not in taken_names:
                return name
            else:
                print(f'{name} is taken. You should choose a more original name.')

    def get_player_ship(other_players: Iterable['Player']):
        ship_name_list = []
        ship_length_list = []
        with open(sys.argv[1]) as fil:
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]

            ship_names, ship_lengths = zip(*all_these_ships)

            for name in ship_names:
                ship_name_list.append(name)
            # print(ship_name_list)

            for length in ship_lengths:
                ship_length_list.append(length)
            # print(ship_length_list)
            return ship_name_list, ship_length_list
    '''
    def place_ship(self):
        ship_name_list = self.get_player_ship()
        print(ship_name_list)
        for i, name in enumerate(ship_name_list):
            place_ship = input(f'where do you want to place your {name} ship in row, col?: ')

            try:
                row, col = place_ship.split(',')
            except:
                print(f'{place_ship} is not in the form row, col')

            try:
                row = int(row)
            except:
                print(f'row needs to be an integer. {row} is not an integer')

            try:
                col = int(col)
            except:
                print(f'col needs to be an integer. {col} is not an integer')

            return row, col

            # print(name, i)

        # return ship_name_list, ship_length_list
        '''

    #def place_ship(self):
        #for ship in self.ship[0]:
            #print(ship)
            # Board.place_ship(ship)




    def turn(self, board: 'board.Board'):
        while True:
            try:
                move = self.get_move()
                move.make(board)
            except:
                print(f"you can't make that move")

    def get_move(self) -> "Move":
        ship_name_list = self.get_player_ship()
        #print(ship_name_list)
        for i, names in enumerate(ship_name_list):
            for name in names:
                place_ship = input(f'where do you want to place your {name} ship in row, col?: ')

                try:
                    row, col = place_ship.split(',')
                except:
                    print(f'{place_ship} is not in the form row, col')

                try:
                    row = int(row)
                except:
                    print(f'row needs to be an integer. {row} is not an integer')

                try:
                    col = int(col)
                except:
                    print(f'col needs to be an integer. {col} is not an integer')

            #return row, col
        #str_move = input(f'{self} enter where you want to play in the form row, col: ')
        return Move.from_str(self, place_ship)

        '''
        def take_turn(self, the_board: "Board") -> None:
            while True:
                try:
                    move = self.get_move()
                    move.make(the_board)
                    return
                except MoveError as error:
                    print(error)

        def get_move(self) -> "Move":
            str_move = input(f'{self} enter where you want to play in the form row, col: ')
            return Move.from_str(self, str_move)
        
        # def turn(self):
        # while True:
        # print(self.board)
        # self.shoot
        # self.did_i_win
        ...
    '''

'''
idk how the move class works 

    def turn(self, player_board: "Board") -> None:
        while True:
            try:
                move = self.get_move()
                move.make(player_board)
                return
            except MoveError as error:
                print(error)

    def get_move(self) -> "Move":
        str_move = input(f'{self} enter where you want to play in the form row, col: ')
        return Move.from_str(self, str_move)


    def whats_the_move(self):
        while True:
            where_to_shoot = input(
                "where we droppin' bois? enter in row, col format: "
            )
        ...

    def __str__(self) -> str:
        return self.name
'''

if __name__ == '__main__':
    board = Board(5, 5)
    test = Player('nes', 5, 5)

    print(test.get_player_board())
