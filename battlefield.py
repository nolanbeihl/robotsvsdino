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
        
    #trying to make a random pick from the fleet and heard to attack
        # self.robo_turn(random.choice(self.fleet.robots).weapon.attack_power)
        # self.dino_turn(random.choice(self.herd.dinosaurs).attack_power)

    def dino_turn(self):
        if self.fleet.robots[0].health > 0:
            Dinosaur.attack(self.herd.dinosaurs[0], self.fleet.robots[0])
        elif self.fleet.robots[1].health >0:
            Dinosaur.attack(self.herd.dinosaurs[1], self.fleet.robots[1])
        elif self.fleet.robots[2].health >0:
            Dinosaur.attack(self.herd.dinosaurs[2], self.fleet.robots[2])

    def robo_turn(self):
        if self.herd.dinosaurs[0].health > 0:
            Robot.attack(self.fleet.robots[0], self.herd.dinosaurs[0])
        elif self.herd.dinosaurs[1].health > 0:
            Robot.attack(self.fleet.robots[1], self.herd.dinosaurs[1])
        elif self.herd.dinosaurs[2].health > 0:
            Robot.attack(self.fleet.robots[2], self.herd.dinosaurs[2])
        else:
            print('All of the dinosaurs have been defeated')
        
        # robot = Robot.attack(random.choice(self.herd.dinosaurs))

    def show_dino_opponent_options(self):
        print((self.herd.dinosaurs[0].name), (self.herd.dinosaurs[1].name), (self.herd.dinosaurs[2].name))

    def show_robo_opponent_options(self):
        print((self.fleet.robots[0].name), (self.fleet.robots[1].name), (self.fleet.robots[2].name))

    def display_winners(self):
        pass

