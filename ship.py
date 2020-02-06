import sys
from typing import Iterable, TypeVar


class Ship(object):

    def __init__(self, name, length):
        self.name = name
        self.length = length
        ...


    def got_hit(self, player):
        self.length -= 1
        print(f"You hit {player}'s {self.name}!")
        if self.length == 0:
            print(f"You destroyed {player}'s {self.name}")

