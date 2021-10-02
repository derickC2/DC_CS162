import random

class Player:

    def __init__(self):
        self.level = 1
        self.health = 100

        self.strength = 5 + random.randrange(0,6)
        self.intelligence = 5 + random.randrange(0,6)
        self.fortitude = 5 + random.randrange(0,6)
