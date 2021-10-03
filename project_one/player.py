import random

class Player:

    def __init__(self):
        self.level = 1
        self.absorb = 0

        self.strength = 5 + random.randrange(0,6)
        self.intelligence = 5 + random.randrange(0,6)
        self.fortitude = 5 + random.randrange(0,6)

        self.health = self.fortitude * 10

    def level_up(self, skill):
        self.level += 1
        self.health += self.fortitude

        if skill == 1: #Strength
            self.strength += 1
        elif skill == 2: #Intelligence
            self.intelligence += 1
        else: #fortitude
            self.fortitude += 1

    def attack(self):
        damage = self.strength + random.randrange(1,5)
        print(f"You do {damage} physical damage!")
        return damage

    def cast(self):
        damage = self.intelligence + random.randrange(1,5)
        print(f"You do {damage} magic damage!")
        return damage

    def protect(self):
        self.absorb += self.fortitude + random.randrange(1,5)
        print(f"You gain a shield. You will absorb the next {self.absorb} damage!")
    
    def inspect_character(self):
        print(f"Your character is  level {self.level}")
        print(f"You will absorb the next {self.absorb} damage!")
        print(f"Stats:")
        print(f"Player health: {self.health}\n"
              f"Player strength: {self.strength}\n"
              f"Player Intelligence: {self.intelligence}\n"
              f"Player Fortitude: {self.fortitude}")