weapon_options = []

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)    

    def weapons_build():
        while len(weapon_options) < 1:
            weapon1 = (Weapon('sword', 10))
            weapon_options.append(weapon1)
        while len(weapon_options) < 2:
            weapon2 = (Weapon('gun', 25))
            weapon_options.append(weapon2)
        while len(weapon_options) < 3:
            weapon3 = (Weapon('laser', 100))
            weapon_options.append(weapon3)
        while len(weapon_options) < 4:
            weapon4 = (Weapon('love', 5))
            weapon_options.append(weapon4)
        return
