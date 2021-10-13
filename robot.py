from weapon import Weapon
from fleet import Fleet
class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = int(health)
        self.weapon = weapon

    def attack(self, dinosaur):
        dinosaur.health - self.weapon.weapon.Weapon.attack_power
        print(f' {dinosaur} health is now {dinosaur.health}')


    
