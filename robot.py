from weapon import Weapon
from fleet import Fleet

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = int(health)
        self.weapon = weapon

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(dinosaur.health)


    
