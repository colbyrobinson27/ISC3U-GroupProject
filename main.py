import random
import tkinter as tk
import EnemyData as eD
root = tk.Tk()
import Biomes as bI
import Binding as binding
import math


#Hello! This is the home base for operations of the game. The structure below is known as a class, and is where we put all of the things that are in the game.
class App():
    #This here is the initialization function. It is what is run when the class is initially started, and is where we initialize all of the local variables being used here
    def __init__(self):
        #This is where we create the tkinter, or GUI, window. We do this through the tkinter class, which we have imported as tk as seen below
        global C1, enemyList
        #This sets the size of the tkinter window
        root.geometry("1280x720")
        #This is the canvas, which is where all of the graphics for the game are painted
        C1 = tk.Canvas(root)
        C1.pack()
        self.width = 100
        self.height = 100
        self.mapHeight = 360
        self.mapWidth = 360
        C1.place(width = self.mapWidth,height = self.mapHeight, x = 460, y = 0)
        C1.config(bg = "Black")
        #This initializes our positioning variables, which are not a python built in, and so must be changed manually throughout the scripts... remember that!

        self.PX = 50
        self.PY = 50
        self.VIEWRANGE = 5
        self.VIEWMAP = [[0 for i in range(self.width)] for j in range(self.height)]
        self.DRAWRANGE = self.mapWidth // 24
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


        #This is the map list; it is where we put all of the 0s and 1s that make up the cave walls and floors

        #This is the size of the map, it is used for all kinds of calculations and for generating the map
        self.mapsize = 100
        bI.Biome.hostility = 100
        bI.createSegment("cave",100,100,True,True,True,True,bI.mapx,bI.mapy)
        bI.createSegment("cave", 1, 1, False, False, False, False, 10, 11)
        bI.createSegment("cave", 1, 1, False, False, False, False, 10, 9)
        bI.createSegment("cave", 1, 1, False, False, False, False, 11, 10)
        bI.createSegment("cave", 1, 1, False, False, False, False, 9, 10)
        #print(bI.Biome.hostility)
        #print(bI.areaList[bI.mapy][bI.mapx].hostility)
        self.map = bI.areaList[bI.mapy][bI.mapx].map
        #This forloor draws everything that is in the self.map variable to the screen (tk.C1). It uses a camera offset of 7 x and 7 y tiles in order to set the players position onscreen equal to the self.PX and self.PY variables
        #for i in range(self.mapsize):
         #   for g in range(len(self.map[i])):
          #      if (self.map[i][g] == "CaveWall-Middle"):
           #         C1.create_image(g*24+12-self.PX + 7*24,i*24+12-self.PY + 7*24,image = self.wallImage)
            #    else:
             #       C1.create_image(g*24+12-self.PX + 7*24,i*24+12-self.PY + 7*24,image = self.floorImage)
        self.draw()

        self.spawnMonsters(18,18)
        for i in range(len(enemyList)):
            #if self.VIEWMAP[enemyList[i].y][enemyList[i].x] == 0:
                #print(enemyList[i].x)
            C1.create_image((enemyList[i].x-self.PX)*24 + 7*24 + 12,(enemyList[i].y-self.PY)*24 + 7*24 + 12, image = enemyList[i].img)
        print(len(enemyList))
        #print(C1.coords(enemyList[len(enemyList)-1].pos))
        #We tag all of the pieces of the map as "map" now so that we can move them all without moving the player, as instead of moving a player and having to redraw the screen
        #we can simply move the tiles around the player to give semblence of movement
        C1.addtag_all("map")
        #Here we draw the player in the center of the screen
        #self.playerImage = C1.create_image(180,180,image = self.player)

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
        try:
            self.map[self.PY][self.PX-1].CODE = self.map[self.PY][self.PX-1].CODE
        except:
            self.loadSection("-x")
            return
        if self.PX<= 0:
            self.loadSection("-x")
        elif self.cML:
            self.PX -= 1
            C1.delete("all")
            self.draw()
            self.cML = False

    def onRightPress(self,*args):
        try:
            self.map[self.PY][self.PX+1].CODE = self.map[self.PY][self.PX+1].CODE
        except:
            self.loadSection("+x")
            return
        if self.PX >= self.width-1:
            self.loadSection("+x")
        elif self.cMR:
            self.PX +=1
            C1.delete("all")
            self.draw()
            self.cMR = False
    def onUpPress(self,*args):
        try:
            self.map[self.PY-1][self.PX].CODE = self.map[self.PY-1][self.PX].CODE
        except:
            self.loadSection("-y")
            return
        if self.PY <= 0:
            self.loadSection("-y")
        elif self.cMU:
            self.PY -= 1
            C1.delete("all")
            self.draw()
            self.cMU = False
    def onDownPress(self,*args):
        try:
            self.map[self.PY+1][self.PX].CODE = self.map[self.PY+1][self.PX].CODE
        except:
            self.loadSection("+y")
            return
        if self.PY >= self.height-1:
            self.loadSection("+y")
        elif self.cMD:
            self.PY += 1
            C1.delete("all")
            self.draw()
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
        #bI.areaList[11][10] = bI.Biome("cave",100,100,True,True,True,True)

        C1.delete('all')
        if dir == "+y":
            bI.mapy +=1
            self.PY = 0

        if dir == "-y":
            bI.mapy -=1
            self.PY = len(bI.areaList[bI.mapy][bI.mapx].map)-1
        if dir == "+x":
            bI.mapx +=1
            self.PX = 0
        if dir == "-x":
            bI.mapx -=1
            self.PX = len(bI.areaList[bI.mapy][bI.mapx].map[self.PY//24])


        #print(bI.areaList[11][10].biome)
        #print(bI.areaList[11][10].map)
        self.map = bI.areaList[bI.mapy][bI.mapx].map
        #for i in range(len(self.map)):
          #  for g in range(len(self.map[i])):
           #     if (self.map[i][g] == "CaveWall-Middle"):
            #        C1.create_image(g*24+12-self.PX + 7*24,i*24+12-self.PY + 7*24,image = self.wallImage)
             #   else:
              #      C1.create_image(g*24+12-self.PX + 7*24,i*24+12-self.PY + 7*24,image = self.floorImage)
        self.draw()

    def NPCInteractions(self,*args):
        response = eD.eNT(self.PX,self.PY,enemyList)
        if response != "":
            if response == "FatBat":
                print("wow")
                battle1 = binding.Battle(root)
                eD.FatBat(3)
    def spawnMonsters(self,xscan,yscan):
        spawned = False
        yZones = len(self.map)//yscan

        for i in range(yZones):
            xZones = len(self.map[i])//xscan
            for g in range(xZones):
                spawned = False
                for h in range(yscan):
                    if spawned != True:
                        for b in range(xscan):
                            if spawned != True:
                                if self.map[i*yscan+h][g*xscan+b].CODE == 0:
                                    enemyList.append(eD.Enemy("FatBat",g*xscan+b,i*yscan+h ))
                                    print(g*xscan+b,i*yscan+h)
                                    spawned = True

    def calcFOV(self):  #By Rhys
        print('RAN')
        for i in range(360):
            ax = math.sin(i)
            ay = math.cos(i)
            x = self.PX
            y = self.PY
            for j in range(self.VIEWRANGE):
                x += ax
                y += ay
                try:
                    self.VIEWMAP[int(round(y))][int(round(x))] = 0
                    if self.map[int(round(y))][int(round(x))].CAN_SEE == False:
                        #print(True)

                        break
                    elif x < 0 or y < 0 or x > self.width or y > self.height:
                        break
                except:
                    continue
           # print(self.VIEWMAP)

    def draw(self):  #By Rhys
        self.VIEWMAP = [[0 for i in range(self.width)] for j in range(self.height)]
        #self.calcFOV()
        try:
            self.VIEWMAP[self.PY][self.PX] = 0
        except:
            print()
        yCTR = 0

        xCTR = 0
        P = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
        print(self.PX,self.PY)
        #print(self.PY-self.DRAWRANGE)
        for y in range((self.PY - self.DRAWRANGE//2), (self.PY + self.DRAWRANGE//2 + 1)):
            xCTR = 0
            for x in range((self.PX - self.DRAWRANGE//2), (self.PX + self.DRAWRANGE//2 + 1)):

                try:
                    if self.VIEWMAP[y][x] == 0:
                        if x > self.width - 1 or x < 0 or y > self.height-1 or y < 0:
                            xCTR += 1
                            continue
                        else:

                            C1.create_image(xCTR * 24 + 12, yCTR * 24 + 12, image=self.map[y][x].IMAGE_DIR)
                            xCTR += 1
                except:
                    xCTR += 1




            yCTR += 1


        for i in range(len(enemyList)):
            #if self.VIEWMAP[enemyList[i].y][enemyList[i].x] == 0:
                #print(enemyList[i].x)
            C1.create_image((enemyList[i].x-self.PX)*24 + 7*24 + 12,(enemyList[i].y-self.PY)*24 + 7*24 + 12, image = enemyList[i].img)
        C1.create_image(180,180,image = self.player)

app = App()
app.run()