from seaBattle import *

game = fullgame(10,1)

aship = game.boarda.ships[0]

bship = game.boardb.ships[0]

list = game.boarda.board

for i in list:
    print(i)

game.boarda.placeships()

for i in list:
    print(i)

aship.move(1,1)
aship.rotate()

game.boarda.placeships()

# so to make this ez i guess what im gonna do is have the ships cease to be after being placed
#instead each individual thing is a ship they just happen to be rignt next to each other

for i in list:
    print(i)

game.boarda.attack([1,1])




