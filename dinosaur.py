class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = int(health)

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        if robot.health > 0:
            print(f'Robot {robot.name} now has a health value of {robot.health}')
        else:
            print(f'Robot {robot.name} has passed away')

