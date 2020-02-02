import sys
from typing import Iterable, TypeVar


class Ship(object):

    def __init__(self, name, length):
        ...

    def ship_health_points(self, ship_length):
        hp = len(ship_length)
        if self.hit():
            hp -= 1
        ...

    def hit(self):
        ...








'''
    def __init__(self, ship_name: str, ship_length: int) -> None:
        self.ShipName = ship_name
        self.ShipLength = ship_length

    def ship_name(self):
        with open(sys.argv[1]) as fil:
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]
            for i in all_these_ships:
                name, length = i[0], i[1]
            return name

    def ship_length(self):
        with open(sys.argv[1]) as fil:
            all_these_ships = [list(line.split()) for line in fil.readlines()[1:]]
            for i in all_these_ships:
                name, length = i[0], i[1]
            return length

        #return ship_name, ship_length

    # def ship_length(self, *args):
    # pass

'''