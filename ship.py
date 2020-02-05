import sys
from typing import Iterable, TypeVar


class Ship(object):

    def __init__(self, name, length):
        self.name = name
        self.length = length
        ...


    def got_hit(self):
        self.length -= 1
        print('u got me!!')
        if self.length == 0:
            print(f'you sunk {self.name} ship!!! :(')

