import random
import tkinter as tk
import EnemyData as eD
import Biomes as bI
import Binding as binding
root = tk.Tk()
#Hello! This is the home base for operations of the game. The structure below is known as a class, and is where we put all of the things that are in the game.
class App():
    #This here is the initialization function. It is what is run when the class is initially started, and is where we initialize all of the local variables being used here
    def __init__(self):
        #This is where we create the tkinter, or GUI, window. We do this through the tkinter class, which we have imported as tk as seen below
        global C1, enemyList
        #This sets the size of the tkinter window
        root.geometry("1400x804")
        #This is the canvas, which is where all of the graphics for the game are painted
        C1 = tk.Canvas(root)
        C1.pack()
        C1.place(width = 360,height = 360, x = 0, y = 0)
        C1.config(bg = "Black")
        #This initializes our positioning variables, which are not a python built in, and so must be changed manually throughout the scripts... remember that!
        self.x = 2160
        self.y = 2160
        self.mapx = 10
        self.mapy = 10
        enemyList = []

        self.cMD = True
        self.cMR = True
        self.cML = True
        #Here is just variables that are used to stop players from holding down a key and moving extremely fast, not too much to worry about
        self.cMU = True
        #These are keybinds. They use tkinter to bind certain keys to certain functions. We have bound all arrow keys on press and on release at the moment
        root.bind("<Left>",self.onLeftPress)
        root.bind("<Right>",self.onRightPress)
        root.bind("<Up>", self.onUpPress)
        root.bind("<Down>", self.onDownPress)
        root.bind("<z>",self.NPCInteractions)
        root.bind("<KeyRelease-Left>",self.onLeftUp)
        root.bind("<KeyRelease-Right>", self.onRightUp)
        root.bind("<KeyRelease-Down>", self.onDownUp)
        root.bind("<KeyRelease-Up>", self.onUpUp)
        #this is where we import images from the game folder, and assign them to variables
        self.floorImage = tk.PhotoImage(file = ".\GrassFloor1.png")
        self.wallImage = tk.PhotoImage(file = ".\WallSketch5.png")
        self.player = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
        self.areaList = []
        for i in range(50):
            self.areaList.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        #This is the map list; it is where we put all of the 0s and 1s that make up the cave walls and floors

        #This is the size of the map, it is used for all kinds of calculations and for generating the map
        self.mapsize = 100
        self.areaList[self.mapy][self.mapx] = bI.Biome("cave",100,100)
        self.map = self.areaList[self.mapy][self.mapx].map
        #This forloor draws everything that is in the self.map variable to the screen (tk.C1). It uses a camera offset of 7 x and 7 y tiles in order to set the players position onscreen equal to the self.x and self.y variables
        for i in range(self.mapsize):
            for g in range(self.mapsize):
                if (self.map[i][g] == "CaveWall-Middle"):
                    C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.wallImage)
                else:
                    C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.floorImage)
        enemyList.append(eD.Enemy(C1,"FatBat"))


        #We tag all of the pieces of the map as "map" now so that we can move them all without moving the player, as instead of moving a player and having to redraw the screen
        #we can simply move the tiles around the player to give semblence of movement
        C1.addtag_all("map")
        #Here we draw the player in the center of the screen
        self.playerImage = C1.create_image(180,180,image = self.player)
        self.timer_tick()
    def run(self):
        root.mainloop()

    def timer_tick(self):


        root.after(50,self.timer_tick)
    def nextTo(self,list,x,y,n):
        ans = 0
        if  x > 0 and list[y][x-1] == n :
            ans +=1
        if x < self.mapsize-1 and list[y][x+1] == n :
            ans +=1
        if  x > 0 and y > 0 and list[y-1][x-1] == n :
            ans +=1
        if  y > 0 and list[y-1][x] == n :
            ans +=1
        if  y > 0 and x < self.mapsize-1 and list[y-1][x+1] == n :
            ans +=1
        if  y < self.mapsize-1 and x < self.mapsize-1 and list[y+1][x+1] == n:
            ans +=1
        if y < self.mapsize-1 and list[y+1][x] == n :
            ans +=1
        if  x > 0 and y < self.mapsize-1 and list[y+1][x-1] == n :
            ans +=1
        return ans



    def onLeftPress(self,*args):
        if self.x <= 0:
            self.loadSection("-x")
        elif self.cML and self.map[self.y//24][(self.x-24)//24] != "CaveWall-Middle":
                C1.move("map", 24, 0)
                self.x -= 24
        self.cML = False

    def onRightPress(self,*args):
        if self.x >= - 24 + self.mapsize * 24:
            self.loadSection("+x")
        if self.cMR and self.map[self.y//24][(self.x+24)//24] != "CaveWall-Middle":
                C1.move("map", -24, 0)
                self.x += 24
        self.cMR = False
    def onUpPress(self,*args):
        if self.y <= 0:
            self.loadSection("-y")
        elif self.cMU and self.map[(self.y-24)//24][self.x//24] != "CaveWall-Middle":
                C1.move("map", 0, 24)
                self.y -= 24
        self.cMU = False
    def onDownPress(self,*args):
        #print((self.y+24)//24,self.x//24)
        if self.y >=  - 24 + self.mapsize * 24:
            self.loadSection("+y")
        elif self.cMD and self.map[(self.y+24)//24][self.x//24] != "CaveWall-Middle":
                C1.move("map", 0, -24)
                self.y+=24
        self.cMD = False
    def onLeftUp(self,*args):
        self.cML = True
    def onRightUp(self,*args):
        self.cMR = True
    def onDownUp(self,*args):
        self.cMD = True
    def onUpUp(self,*args):
        self.cMU = True
    def loadSection(self,dir):
        print("hi")
        self.areaList[11][10] = bI.Biome("cave",100,100)

        C1.delete('all')
        if dir == "+y":
            self.mapy +=1
            self.y = 0

        if dir == "-y":
            self.mapy -=1
            self.y = len(self.areaList[self.mapy][self.mapx])*24 -24
        if dir == "+x":
            self.mapx +=1
            self.x = 0
        if dir == "-x":
            self.map -=1
            self.x = len(self.areaList[self.mapy][self.mapx][0])*24 -24
        self.map = self.areaList[self.mapy][self.mapx]
        for i in range(self.mapsize):
            for g in range(self.mapsize):
                if (self.map[i][g] == "CaveWall-Middle"):
                    C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.wallImage)
                else:
                    C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.floorImage)
        C1.addtag_all("map")
        C1.create_image(180, 180, image=self.player)
    def NPCInteractions(self,*args):
        response = eD.eNT(self.playerImage,enemyList,C1)
        if response != "":
            if response == "FatBat":
                eD.FatBat()
                battle1 = binding.Battle(root)
app = App()
app.run()