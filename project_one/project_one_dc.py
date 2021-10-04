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

    def attack(self, target):
        damage = self.strength + random.randrange(1,5)
        print(f"You do {damage} physical damage!")
        target.get_attacked(damage)

    def cast(self, target):
        damage = self.intelligence + random.randrange(1,5)
        print(f"You do {damage} magic damage!")
        target.get_attacked(damage)

    def protect(self):
        self.absorb += self.fortitude + random.randrange(1,5)
        print(f"You gain a shield. You will absorb the next {self.absorb} damage!")

    def get_attacked(self, damage):
        if self.absorb >= damage:
            self.absorb = self.absorb - damage
            print("Your shield absorbed the damage")
            print(f"You have {self.absorb} damage remaining in your shield")
        else:
            damage = damage - self.absorb
            print(f"You absorb {self.absorb} damage, and take {damage} damage.")
            self.absorb = 0
            self.health = self.health - damage
            print(f"You have {self.health} remaining health.")
        
    def inspect_character(self):
        print(f"Your character is  level {self.level}")
        print(f"You will absorb the next {self.absorb} damage!")
        print(f"Stats:")
        print(f"Player health: {self.health}\n"
              f"Player strength: {self.strength}\n"
              f"Player Intelligence: {self.intelligence}\n"
              f"Player Fortitude: {self.fortitude}")

class Goblin:

    def __init__(self):
        self.health = 50
        self.base_damage = 5
        self.dead = False

    def get_attacked(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        if self.health == 0:
            dead = True

        return self.dead

    def attack(self, target):
        damage = self.base_damage + random.randrange(1,4)
        target.get_attacked(damage)
        

    def get_health(self):
        print(f"The goblin has {self.health} health remaining.")


def __main__():
    a_player = Player()
    a_goblin = Goblin()

    a_player.inspect_character()

    a_player.attack(a_goblin)
    a_goblin.get_health()
    a_goblin.attack(a_player)


if __name__ == "__main__":
    __main__()
