from robot import Robot
from weapon import Weapon
from weapon import weapon_options
armory = Weapon.weapons_build()
weapon_options.append(armory)


robot_choices = []
robots = Robot('Wallie', 200,weapon_options[0])
robot_choices.append(robots)
robots = Robot('Johny 5', 200,weapon_options[3])
robot_choices.append(robots)
robots = Robot('T1000', 500, weapon_options[2])
robot_choices.append(robots)

class Fleet:
    def __init__(self):
        self.robots = []
        #self.build_fleet()        
        
    def build_fleet(self):
        fleet1 = []
        while len(fleet1) <3:
            print('Please choose your robots : ')
            i = 1
            for robots in robot_choices:
                print(f"\n\t Enter -{i} for {robots.name}")
                i+=1
            user_selection = input("Selection:")
            choosen_one = int(user_selection)
            fleet1.append(robot_choices[choosen_one - 1])
            if len(fleet1) == 3:
                print('Your Fleet has been created')
                return fleet1

            
    def try_parse_int(value):
        """Attempts to parse a string into an integer, returns 0 if unable to parse"""
        try:
            return int(value)
        except:
            return 0
                