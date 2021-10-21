

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.weapon_options = []    

    def weapons_build(self):
        while len(self.weapon_options) < 1:
            weapon1 = (Weapon('sword', 10))
            self.weapon_options.append(weapon1)
        while len(self.weapon_options) < 2:
            weapon2 = (Weapon('gun', 25))
            self.weapon_options.append(weapon2)
        while len(self.weapon_options) < 3:
            weapon3 = (Weapon('laser', 100))
            self.weapon_options.append(weapon3)
        while len(self.weapon_options) < 4:
            weapon4 = (Weapon('love', 5))
            self.weapon_options.append(weapon4)
        return
