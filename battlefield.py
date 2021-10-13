from main import herd1
from main import fleet1


class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd

    def run_game(self):
        self.display_welcome()

        pass

    def display_welcome(self):
        print('Welcome to todays match between Robots and Dinosaurs')
        print('Today for the dinosaurs we have' self.show_dino_opponent_options())
    def battle(self):
        pass

    def dino_turn(self,dinosaur):

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        print((herd1[0]), (herd1[1]), (herd1[2]))

    def show_robo_opponent_options(self):
        print((fleet1[0]), (fleet1[1]), (fleet1[2]))

    def display_winners(self):
        pass

