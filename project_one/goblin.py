import random

class Goblin:

    def __init__(self):
        self.health = 50
        self.base_damage = 5
        self.dead = False

    def get_attacked(self, attack):
        self.health = self.health - attack

        if self.health <= 0:
            dead = True
        
        return self.dead

    def attack(self, target):
        damage = self.base_damage + random.randrange(1,4)
        target.get_attacked(damage)
        

    def get_health(self):
        print(f"The goblin has {self.health} health remaining.")
