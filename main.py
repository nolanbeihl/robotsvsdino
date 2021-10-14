from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield



weapon1 = Weapon('sword', 10)
weapon2 = Weapon('gun', 25)
weapon3 = Weapon('laser', 100)
weapon4 = Weapon('love', 5)

robot1 = Robot('Wallie', 200, weapon4)
robot2 = Robot('Johhn 5', 200, weapon3)
robot3 = Robot('T1000', 500, weapon2)

dinosaur1 = Dinosaur('T-Rex', 50, 200)
dinosaur2 = Dinosaur('Blue', 100, 300)
dinosaur3 = Dinosaur('Tragdor', 150, 250)

fleet1 = Fleet()
herd1 = Herd()
game = Battlefield(fleet1,herd1)

fleet1.create_fleet(robot1)
fleet1.create_fleet(robot2)
fleet1.create_fleet(robot3)

herd1.create_herd(dinosaur1)
herd1.create_herd(dinosaur2)
herd1.create_herd(dinosaur3)




print(game.display_welcome())




