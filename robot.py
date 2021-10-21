from weapon import Weapon


class Robot(Weapon):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = int(health)
        self.weapon = Weapon.weapon_options.index()

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        if dinosaur.health > 0:
            print(f'Dinosaur {dinosaur.name} now has a health of {dinosaur.health}')
        else: 
            print(f' Dinosaur {dinosaur.name} has died')


    
