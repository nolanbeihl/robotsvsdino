from herd import Herd
from fleet import Fleet
import random

class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd

    def run_game(self):
        self.display_welcome()
        pass

    def display_welcome(self):
        print('Welcome to todays match between Robots and Dinosaurs')
    
    def battle(self):
        self.robo_turn
        # self.dino_turn
        pass

    # def dino_turn(self,dinosaur):
    #     dinosaur = random(self.herd[])
    #     pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        print((self.herd.dinosaurs[0].name), (self.herd.dinosaurs[1].name), (self.herd.dinosaurs[2].name))

    def show_robo_opponent_options(self):
        print((self.fleet.robots[0].name), (self.fleet.robots[1].name), (self.fleet.robots[2].name))

    def display_winners(self):
        pass

