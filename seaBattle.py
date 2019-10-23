class boat():
    def __init__(self, length):
        self.length = length
        self.rotation = 0
        self.location = [0,0]
        self.destroyed = False
        self.rep = [1]*self.length
    def hit(self, part):
        self.rep[part] = 2


    def sink(self):
        self.destroyed = True
        self.rep = [2] * self.length
    def isDead(self):

        self.destroyed = self.rep = [2]*self.length
        return self.destroyed
    def move(self, x, y):
        self.location[0]+=x
        self.location[1] +=y
    def rotate(self):
        self.rotation +=1
        self.rotation %=2



class board():

    def __init__(self, s, ns):
        self.size = s
        self.board = []
        self.ships = [boat(2)]
        self.alive = True
        self.board = []
        for i in range(self.size):
            self.board.append([None]*self.size)
        return

    def isAlive(self):
        for i in self.board:
            if 1 in i:
                return True
        return False

    def getMovement(self):
        pass



    # do not not not run this after the person is done moving the ships

    def moveships(self):
        for i in range(len(self.ships)):
            movingship = True
            while movingship:
                movement = self.getMovement()
                if movement == [0,0]:
                    movingship = False
                else:
                    self.ships[i].move(movement)
                    self.placeships()

    def placeships(self):
        for i in range (self.size):
            for j in range(self.size):
                self.board[i][j] = None

        for i in self.ships:
            print(i.location)
            for j in range(i.length):
                if i.rotation == 0:
                    self.board[i.location[0]+j][i.location[1]] = i.rep[j]
                else:
                    self.board[i.location[0]][i.location[1]+j] = i.rep[j]

# so the way this works
    # 1 u got the bot dms a blank board to eacn and they place pieces
    # 2 the first player is up he sess a unattacked board and aims and fires in the chat he saw.
    #3 the board gets edited for player 2 and he repeats
    # (as ships are sunk its also updated in dms)
    # when there is winner the main board area gets delete and in its place goes a u win
    # idk what else i need furure me when u see this i hope ur not confused but its like 5 and im tired af lemme sleep

    def showboard(self):
        pass



class fullgame():
    def __init__(self, size, numship):
        self.currentplayer = 0
        self.size = size
        self.boarda = board(self.size, numship)
        self.boardb = board(self.size, numship)


    def getboard(self):
        return self.currentplayer%2==0 and self.boarda or self.boardb

    def check(self, pos, board):
        return board[pos[0]][pos[1]] is not None

    def turn(self, attack):
        self.check(attack, self.getboard())
        self.currentplayer+=1
        self.currentplayer5=2








# to the player:
# none and 0 both show up as water, 1 is ship and 2 is shipit(fire)

#to the opponent
# none is ? 0 is miss (water)  1 is not present (shows as none or ?) 2 is shiphit (fire)

'''
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
❔❔❔❔❔❔❔❔❔❔❔
'''


