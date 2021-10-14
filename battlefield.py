from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd

    def run_game(self):
        self.display_welcome()

        pass

    def display_welcome(self):
        print('Welcome to todays match between Robots and Dinosaurs')
        print((f'Today for the dinosaurs we have') (self.show_dino_opponent_options(self)))
    
    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        self.herd = ((Herd.dinosaurs[0]), (Herd.dinosaurs[1]), (Herd.dinosaurs[2]))
        print(self.herd)

    def show_robo_opponent_options(self):
        self.fleet = ((Fleet.robots[0]), (Fleet.robots[1]), (Fleet.robots[2]))
        print(self.fleet)

    def display_winners(self):
        pass

