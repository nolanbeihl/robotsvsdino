from weapon import Weapon
from fleet import Fleet
from herd import Herd

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = int(health)
        self.weapon = weapon

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        if dinosaur.health > 0:
            print(f'Dinosaur {dinosaur.name} now has a health of {dinosaur.health}')
        else: 
            Herd.pop(dinosaur)


    
