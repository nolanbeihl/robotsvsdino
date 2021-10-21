from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from weapon import Weapon
from robot import Robot
import random

robot_choices = []

dinosaur1 = Dinosaur('T-Rex', 50, 200)
dinosaur2 = Dinosaur('Blue', 100, 300)
dinosaur3 = Dinosaur('Tragdor', 150, 250)

fleet1 = Fleet()
herd1 = Herd()

class Battlefield:
    def __init__(self,):
        self.fleet = ()
        self.herd = ()

    def run_game(self):
        self.display_welcome()
        self.show_dino_opponent_options()
        self.show_robo_opponent_options()
        self.battle()

    def display_welcome(self):
        print('Welcome to todays match between Robots and Dinosaurs')
    
    def battle(self):
        self.robo_turn()
        self.dino_turn()
        while len(herd1)>0 and len(robot_choices)>0:
            self.robo_turn()
            if herd1[0].health<=0:
                herd1.pop(0)
            elif robot_choices[0] and herd1[0]:
                self.dino_turn()
                if robot_choices[0].health <= 0:
                    robot_choices.pop(0)
            else:
                 self.battle()
        else:
            if herd1[0].health > 0:
                self.display_winners('The Dinosaurs have won')
                print('The battle is over')
            elif robot_choices[0].health > 0:
                self.display_winners('The Robots have won')
                print('The battle is over')

    def dino_turn(self):
        if robot_choices[0].health > 0:
    #use of this randomizer for the characters ends up using dead characters, will continue to work on
            # robot = random.choice(self.fleet.robots)
            # dinosaur = random.choice(self.herd.dinosaurs)
            # Dinosaur.attack(dinosaur,robot)
            Dinosaur.attack(herd1[0], robot_choices[0])
        else:
            return

    def robo_turn(self):
        if herd1[0].health > 0:
            # robot = random.choice(self.fleet.robots)
            # dinosaur = random.choice(self.herd.dinosaurs)
            # Robot.attack(robot, dinosaur)
            Robot.attack(robot_choices[0], robot_choices[0])
        else:
            return
        
    def show_dino_opponent_options(self):
        print((herd1[0].name), (herd1[1].name), (herd1[2].name))

    def show_robo_opponent_options(self):
        print(robot_choices[0].name), (robot_choices[1].name), (robot_choices[2].name)

    def display_winners(self,winner):
        print(winner)
 
    def build_fleet(self):
        fleet1 = robot_choices
        while len(fleet1) <3:
            print('Please choose your robots : ')
            i = 1
            for robots in robot_choices:
                print(f"\n\t Enter -{1} for {robots.name}")
                i+=1
            user_selection = self.try_parse_int(input("Selection:"))
            fleet1.append(user_selection)
        return fleet1

    def try_parse_int(value):
        """Attempts to parse a string into an integer, returns 0 if unable to parse"""
        try:
            return int(value)
        except:
            return 0
            
