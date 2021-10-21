from robot import Robot
from weapon import Weapon
# weapons = Weapon('', 0)
weapon_options = Weapon('',0)
weapon_options.weapon_options.append(weapon_options.weapons_build())


robot_choices = []
robots = Robot('Wallie', 200, [0])
robot_choices.append(robots)
robots = Robot('Johny 5', 200, [3])
robot_choices.append(robots)
robots = Robot('T1000', 500, [2])
robot_choices.append(robots)

class Fleet:
    def __init__(self):
        self.robots = []
        self.build_fleet()        
        
  
    def build_fleet(self):
            fleet1 = self.robots
            while len(fleet1) <3:
                print('Please choose your robots : ')
                i = 1
                for robots in robot_choices:
                    print(f"\n\t Enter -{1} for {robots.name}")
                    i+=1
                user_selection = self.try_parse_int(input("Selection:"))
                fleet1.append(user_selection)
                return fleet1
            else:
                print('Your fleet has been created')


    def try_parse_int(value):
        """Attempts to parse a string into an integer, returns 0 if unable to parse"""
        try:
            return int(value)
        except:
            return 0
                