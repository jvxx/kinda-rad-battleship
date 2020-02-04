import sys
from typing import Iterable
from board import Board
from move import Move


class Player(object):
    def __init__(self, other_players: Iterable["Player"], row, col, blank_char: str = '*') -> None:
        self.row = row
        self.col = col
        self.blank_char = blank_char
        self.board = Board(row, col, blank_char)
        self.name = self.get_player_name(other_players)
        self.ship = self.get_player_ship()

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


    def get_ship_placement(self) -> "Move":
        ship_name_list = self.get_player_ship()[0]
        #print(ship_name_list)

        # whoops it keeps looping back
        ship_size = self.get_ship_parameters()[0]
        ship_name = self.get_ship_parameters()[1]

        ship_coords_dict = {}

        for name in ship_name_list:
            place_ship = input(f'{self} where do you want to place your {name} ship in row, col?: ')

            valid_input = 0

            while valid_input < 3:
                valid_input = 0
                try:
                    row, col = place_ship.split(',')
                    valid_input += 1
                except:
                    print(f'{place_ship} is not in the form row, col')
                    break

                try:
                    row = int(row)
                    valid_input += 1
                except:
                    print(f'row needs to be an integer. that is not an integer')
                    break

                try:
                    col = int(col)
                    valid_input += 1
                except:
                    print(f'col needs to be an integer. that is not an integer')
                    break
            if valid_input == 3:
                ship_coords_dict[row] = col

            #return ship_coords_dict
        return Move.from_str(self, ship_coords_dict, ship_name, ship_size)


    def get_ship_parameters(self):
        ship_name_list = self.get_player_ship()[0]
        ship_length_list = self.get_player_ship()[1]

        for length in ship_length_list:
            ship_size = length
        for name in ship_name_list:
            ship_name = name

        return ship_size, ship_name

    def __str__(self) -> str:
        # convert player name from generator -> str
        return self.name

    def get_player_board(self):
        print(self.board)
        ...


    def initial_turn(self, board: 'Board', row, col) -> None:
        while True:
            try:
                # from ship placement we get the Move class back
                # cls(maker, rol, col, name, length)

                # now we get a list of ship coords back
                move = self.get_ship_placement()
                #move.place_the_damn_ship()
                # move is the class move.Move
                move.make(board)
                move.place_ship_orient()
                move.check_ship(row, col)
                move.place_ship()
                return
            except:
                print(f"you can't make that move")

    def get_move(self) -> 'Move':
        str_move = self.ship_placement
        return Move.from_str(self, str_move)


    def place_all_ships(self):
        '''
        for each_ship in ships:
            board.place_the_damn_ship()
        :return:
        '''
