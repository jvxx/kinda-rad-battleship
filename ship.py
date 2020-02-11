class Ship(object):

    def __init__(self, name: str, length: int) -> None:
        self.name = name
        self.length = length

    def got_hit(self, player: str):
        self.length -= 1
        print(f"You hit {player}'s {self.name}!")
        if self.length == 0:
            print(f"You destroyed {player}'s {self.name}")
