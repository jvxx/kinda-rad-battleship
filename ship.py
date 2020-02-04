import sys
from typing import Iterable, TypeVar


class Ship(object):

    def __init__(self, name, length):
        #self.name = self.ship_name(name)
        #self.health = self.ship_health_points(length)
        self.name = name
        self.length = length
        self.health = self.ship_health_points()
        ...

    def ship_size(self):
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

    def ship_name(self):
        return self.name
        ...

    def ship_health_points(self):
        hp = self.length
        if self.hit():
            hp -= 1
        return hp
        ...

    def hit(self):
        '''
        if input coords
        :return:
        '''
        ...

