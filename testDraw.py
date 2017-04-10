import random
import tkinter as tk
import time
def neighbours(map,x,y):
    d = [[0,-1],[0,1],[-1,0],[1,0],[1,1],[-1,-1],[1,-1],[-1,-1]]
    n = 0
    for i in range(8):
        if map[y+d[i][0]][x+d[i][1]] == 1:
            n += 1
    return n
class Player:
    def __init__(self,X,Y,IMAGE_DIR):

        self.PX = X
        self.PY = Y
player = Player(5,5,".\PlayerPlaceHolder.png")

class App():
    #This here is the initialization function. It is what is run when the class is initially started, and is where we initialize all of the local variables being used here
    def __init__(self):
        #This is where we create the tkinter, or GUI, window. We do this through the tkinter class, which we have imported as tk as seen below
        self.root = tk.Tk()
        #This sets the size of the tkinter window
        self.root.geometry("1000x804")
        #This is the canvas, which is where all of the graphics for the game are painted
        self.C1 = tk.Canvas(self.root)
        self.C1.pack()
        self.C1.place(width = 360,height = 360, x = 0, y = 0)
        self.C1.config(bg = "Black")
        #This initializes our positioning variables, which are not a python built in, and so must be changed manually throughout the scripts... remember that!
        self.x = 216
        self.y = 216
        #Here is just variables that are used to stop players from holding down a key and moving extremely fast, not too much to worry about
        self.cMU = True
        self.cMD = True
        self.cMR = True
        self.cML = True
        #These are keybinds. They use tkinter to bind certain keys to certain functions. We have bound all arrow keys on press and on release at the moment
        self.root.bind("<Left>", self.onLeftPress)
        self.root.bind("<Right>", self.onRightPress)
        self.root.bind("<Up>", self.onUpPress)
        self.root.bind("<Down>", self.onDownPress)

    def onLeftPress(self,*args):
        player.PX -= 1
        print('RAN')
    def onRightPress(self,*args):
        player.PX += 1

    def onUpPress(self,*args):
        player.PY -= 1

    def onDownPress(self,*args):
        player.PY += 1


    def run(self):
        self.root.mainloop()
app = App()
class Tile:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file = IMAGE_DIR)
        self.CODE = CODE
caveFloor = Tile(True,True,".\GrassFloor1.png",0)
caveWall = Tile(False,False,".\WallSketch5.png",1)
tileSet = [caveWall,caveFloor]

class Map:
    def __init__(self,WIDTH,HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.map = [[random.randint(0,1) for i in range(self.WIDTH)]for j in range(self.HEIGHT)]
        self.carveMap(5)
        self.PX = 5
        self.PY = 5
        self.DRAWRANGE = 7
    def carveMap(self,AMT):
        for i in range(AMT):

            for y in range(1, len(self.map) - 1):
                for x in range(1, len(self.map[y]) - 1):
                    if neighbours(self.map, x, y) >= 4 and self. map[y][x] == 1:
                        self.map[y][x] = 1
                    elif neighbours(self.map, x, y) >= 5 and self.map[y][x] == 0:
                        self.map[y][x] = 1
                    else:
                        self.map[y][x] = 0

    def draw(self):
        yCTR = 0

        xCTR = 0
        P = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
        print(player.PY-self.DRAWRANGE)
        for y in range((player.PY - self.DRAWRANGE), (player.PY + self.DRAWRANGE + 1)):
            xCTR = 0
            for x in range((player.PX - self.DRAWRANGE), (player.PX + self.DRAWRANGE + 1)):
                if x > self.WIDTH - 1 or x < 0 or y > self.HEIGHT-1 or y < 0:
                    a = None
                else:
                    for j in range(len(tileSet)):

                        if tileSet[j].CODE == map.map[y][x]:
                            app.C1.create_image(xCTR * 24 + 12, yCTR * 24 + 12, image=tileSet[j].IMAGE_DIR)

                xCTR += 1

            yCTR += 1
        app.C1.create_image(int(xCTR/2) * 24 + 12, int(yCTR/2) * 24 + 12, image=P)
        app.run()




map = Map(100,100)



map.draw()
