import sys
from typing import Iterable, TypeVar


class Ship(object):

    def __init__(self, name, length):
        #self.name = self.ship_name(name)
        #self.health = self.ship_health_points(length)
        self.name = name
        self.length = length
        ...

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
        ...

if __name__ == '__main__':
    test = Ship('dumb', 5)

    print(test.ship_name())


    #test.place_ship_orient('nes')
