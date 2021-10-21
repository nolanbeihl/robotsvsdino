from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd


dinosaur1 = Dinosaur('T-Rex', 50, 200)
dinosaur2 = Dinosaur('Blue', 100, 300)
dinosaur3 = Dinosaur('Tragdor', 150, 250)

fleet1 = Fleet()
herd1 = Herd()
fleet1.build_fleet()

herd1.dinosaurs.append(dinosaur1)
herd1.dinosaurs.append(dinosaur2)
herd1.dinosaurs.append(dinosaur3)

from battlefield import Battlefield

game = Battlefield(fleet1,herd1)

game.run_game()






