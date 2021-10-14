from dinosaur import Dinosaur
from robot import Robot
import random

class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd

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
        while len(self.herd.dinosaurs)>0 and len(self.fleet.robots)>0:
            self.robo_turn()
            if self.herd.dinosaurs[0].health<=0:
                self.herd.dinosaurs.pop(0)
            elif self.fleet.robots[0] and self.herd.dinosaurs[0]:
                self.dino_turn()
                if self.fleet.robots[0].health <= 0:
                    self.fleet.robots.pop(0)
            else:
                 self.battle()
        else:
            if self.herd.dinosaurs[0].health > 0:
                self.display_winners('The Dinosaurs have won')
                print('The battle is over')
            elif self.fleet.robots[0].health > 0:
                self.display_winners('The Robots have won')
                print('The battle is over')

    def dino_turn(self):
        if self.fleet.robots[0].health > 0:
    #use of this randomizer for the characters ends up using dead characters, will continue to work on
            # robot = random.choice(self.fleet.robots)
            # dinosaur = random.choice(self.herd.dinosaurs)
            # Dinosaur.attack(dinosaur,robot)
            Dinosaur.attack(self.herd.dinosaurs[0], self.fleet.robots[0])
        else:
            return

    def robo_turn(self):
        if self.herd.dinosaurs[0].health > 0:
            # robot = random.choice(self.fleet.robots)
            # dinosaur = random.choice(self.herd.dinosaurs)
            # Robot.attack(robot, dinosaur)
            Robot.attack(self.fleet.robots[0], self.herd.dinosaurs[0])
        else:
            return
        
    def show_dino_opponent_options(self):
        print((self.herd.dinosaurs[0].name), (self.herd.dinosaurs[1].name), (self.herd.dinosaurs[2].name))

    def show_robo_opponent_options(self):
        print((self.fleet.robots[0].name), (self.fleet.robots[1].name), (self.fleet.robots[2].name))

    def display_winners(self,winner):
        print(winner)


