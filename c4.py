class C4():
    def __init__(self):
        self.board = []
        for i in range(7):
            x = []
            for j in range(6):
                x.append(None)
            self.board.append(x)

        self.tops = []
        for i in range(7):
            self.tops.append(0)


    def __str__(self):
        out = ""
        board = []
        for i in self.board:
            board.append(i[::-1])
        board = board[::-1]
        bard = zip(*board[::-1])

        for i in bard:
            out +=str(i)
            out +="\n"

        out = out.replace("None",":white_circle: ")
        out = out.replace("1", ":large_blue_circle: " )
        out = out.replace("2", ":red_circle: ")
        out = out.replace(",", "")
        out = out.replace(" ", "")
        out = out.replace("(", "")
        out = out.replace(")", "")
        return out


    def check_horizontal(self):
        streak = 0
        last = None
        winner = None
        for i in self.board:
            for j in i:
                if j == last:
                    streak+=1
                    if streak ==4 and last!=None:
                        winner = last
                else:

                    streak = 1
                    last = j
        return winner


    def check_vertical(self):
        #i can only admit this bc nobody is ever gonna see this comment
        # but i ahve absoultye no idea what this does i just know it work
        flipboard = zip(*self.board[::-1])
        streak = 0
        last = None
        winner = None
        for i in flipboard:
            for j in i:
                if j == last:
                    streak+=1
                    if streak >=4 and last!=None:
                        winner = last
                else:
                    streak = 1
                    last = j
        return winner


    def check_diag_down(self):
        streak = 0
        last = None
        winner = None
        for i in range(0,len(self.board)-4):
            for j in range(0, len(self.board[i]) -4):
                for k in range(4):
                    streak = 0
                    last = None
                    if self.board[i+k][j+k] == last:
                        streak+=1
                        if streak >=4 and last!=None:
                            return last
                    else:
                        streak = 1
                        last = self.board[i+k][j+k]
        return winner

    def check_diag_up(self):
        streak = 0
        last = None
        winner = None
        for i in range(0,len(self.board)-4):
            for j in range(len(self.board[i])-1, 3, -1):
                streak = 0
                last = None
                for k in range(4):
                    if self.board[i+k][j-k] == last:
                        streak+=1
                        if streak >=4 and last!=None:
                            return last
                    else:
                        streak = 1
                        last = self.board[i+k][j-k]
        return winner


    def checkall(self):
        winner = self.check_vertical()
        if winner != None:
            return winner
        winner = self.check_horizontal()
        if winner != None:
            return winner
        winner = self.check_diag_down()
        if winner != None:
            return winner
        winner = self.check_diag_up()
        if winner != None:
            return winner
        return None


    def addp1(self, x):
        self.board[x][self.tops[x]] = 1
        self.tops[x]+=1


    def addp2(self,x):
        self.board[x][self.tops[x]] = 2
        self.tops[x] +=1
