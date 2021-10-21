from weapon import Weapon
from weapon import weapon_options

class Robot(Weapon):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = int(health)
        self.weapon = weapon
        weapon 

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        if dinosaur.health > 0:
            print(f'\nDinosaur {dinosaur.name} now has a health of {dinosaur.health}')
        else: 
            print(f'\nDinosaur {dinosaur.name} has died')


    
