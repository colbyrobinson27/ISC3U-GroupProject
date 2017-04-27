import random
import tkinter as tk
import EnemyData as eD
root = tk.Tk()
import Biomes as bI
import Binding as binding
import math
import pygame


#Hello! This is the home base for operations of the game. The structure below is known as a class, and is where we put all of the things that are in the game.
class App():
    #This here is the initialization function. It is what is run when the class is initially started, and is where we initialize all of the local variables being used here
    def __init__(self):
        pygame.mixer.init()


        self.enemyToRemove = 0
        #This is where we create the tkinter, or GUI, window. We do this through the tkinter class, which we have imported as tk as seen below
        global C1, enemyList
        #This sets the size of the tkinter window
        root.geometry("1280x720")
        #This is the canvas, which is where all of the graphics for the game are painted
        C1 = tk.Canvas(root)
        self.moveSpeed = 150
        C1.pack()
        self.tileSize =32
        self.width = 100
        self.height = 100
        self.mapHeight = self.tileSize*15
        self.mapWidth = self.tileSize*15
        C1.place(width = self.mapWidth,height = self.mapHeight, x = 460, y = 0)
        C1.config(bg = "Black")
        #This initializes our positioning variables, which are not a python built in, and so must be changed manually throughout the scripts... remember that!
        self.treetop = tk.PhotoImage(file="./treetop.png")





        self.moveCounter = 0
        self.batAniCounter = 0

        self.playerDown1 = tk.PhotoImage(file="./Images/Characters/2Down1.png")
        self.playerDown2 = tk.PhotoImage(file="./Images/Characters/2Down2.png")
        self.playerDown3 = tk.PhotoImage(file="./Images/Characters/2Down3.png")
        self.playerDown = [self.playerDown1,self.playerDown2,self.playerDown3,self.playerDown2]

        self.playerLeft1 = tk.PhotoImage(file="./Images/Characters/2Left1.png")
        self.playerLeft2 = tk.PhotoImage(file="./Images/Characters/2Left2.png")
        self.playerLeft3 = tk.PhotoImage(file="./Images/Characters/2Left3.png")
        self.playerLeft = [self.playerLeft1, self.playerLeft2, self.playerLeft3, self.playerLeft2]

        self.playerRight1 = tk.PhotoImage(file="./Images/Characters/2Right1.png")
        self.playerRight2 = tk.PhotoImage(file="./Images/Characters/2Right2.png")
        self.playerRight3 = tk.PhotoImage(file="./Images/Characters/2Right3.png")
        self.playerRight = [self.playerRight1, self.playerRight2, self.playerRight3, self.playerRight2]

        self.playerUp1 = tk.PhotoImage(file="./Images/Characters/2Up1.png")
        self.playerUp2 = tk.PhotoImage(file="./Images/Characters/2Up2.png")
        self.playerUp3 = tk.PhotoImage(file="./Images/Characters/2Up3.png")
        self.playerUp = [self.playerUp1, self.playerUp2, self.playerUp3, self.playerUp2]
        self.aniCounter = 0
        self.PX = 50
        self.PY = 90
        self.VIEWRANGE = 5
        self.VIEWMAP = [[0 for i in range(self.width)] for j in range(self.height)]
        self.DRAWRANGE = self.mapWidth // self.tileSize
        enemyList = []
        self.mL = False
        self.mR = False
        self.mU = False
        self.mD = False
        self.rightTime = 0
        self.leftTime = 1
        self.upTime = 2
        self.downTime = 3

        #Here is just variables that are used to stop players from holding down a key and moving extremely fast, not too much to worry about

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

        root.bind("<a>", self.onLeftPress)
        root.bind("<d>", self.onRightPress)
        root.bind("<w>", self.onUpPress)
        root.bind("<s>", self.onDownPress)
        root.bind("<KeyRelease-a>", self.onLeftUp)
        root.bind("<KeyRelease-d>", self.onRightUp)
        root.bind("<KeyRelease-s>", self.onDownUp)
        root.bind("<KeyRelease-w>", self.onUpUp)
        #this is where we import images from the game folder, and assign them to variables
        self.player= tk.PhotoImage(file = "./Images/Characters/2Down1.png")



        #This is the map list; it is where we put all of the 0s and 1s that make up the cave walls and floors

        #This is the size of the map, it is used for all kinds of calculations and for generating the map
        self.mapsize = 100
        bI.Biome.hostility = 100
        bI.createSegment("cave",100,100,True,True,True,True,bI.mapx,bI.mapy)
        bI.createSegment("forest", 100, 100, False, False, False, False, 10, 11)
        bI.createSegment("forest", 100, 100, False, False, False, False, 10, 9)
        bI.createSegment("forest", 100, 100, False, False, False, False, 11, 10)
        bI.createSegment("forest", 100, 100, False, False, False, False, 9, 10)
        bI.createSegment("desert", 100, 100, False, False, False, False, 9, 11)
        bI.createSegment("custom,littleCave.txt",100,100,False,False,False,False,11,11)
        #print(bI.Biome.hostility)
        #print(bI.areaList[bI.mapy][bI.mapx].hostility)
        bI.areaList[bI.mapy][bI.mapx].music.play(loops=-1)
        self.map = bI.areaList[bI.mapy][bI.mapx].map
        self.scenery = bI.areaList[bI.mapy][bI.mapx].scenery
        #This forloor draws everything that is in the self.map variable to the screen (tk.C1). It uses a camera offset of 7 x and 7 y tiles in order to set the players position onscreen equal to the self.PX and self.PY variables
        #for i in range(self.mapsize):
         #   for g in range(len(self.map[i])):
          #      if (self.map[i][g] == "CaveWall-Middle"):
           #         C1.create_image(g*self.tileSize+12-self.PX + 7*self.tileSize,i*self.tileSize+12-self.PY + 7*self.tileSize,image = self.wallImage)
            #    else:
             #       C1.create_image(g*self.tileSize+12-self.PX + 7*self.tileSize,i*self.tileSize+12-self.PY + 7*self.tileSize,image = self.floorImage)
        self.draw()

        self.spawnMonsters(18,18)
        for i in range(len(enemyList)):
            #if self.VIEWMAP[enemyList[i].y][enemyList[i].x] == 0:
                #print(enemyList[i].x)
            C1.create_image((enemyList[i].x-self.PX)*self.tileSize + 7*self.tileSize + 20,(enemyList[i].y-self.PY)*self.tileSize + 7*self.tileSize + 20, image = enemyList[i].img)
        print(len(enemyList))
        #print(C1.coords(enemyList[len(enemyList)-1].pos))
        #We tag all of the pieces of the map as "map" now so that we can move them all without moving the player, as instead of moving a player and having to redraw the screen
        #we can simply move the tiles around the player to give semblence of movement
        C1.addtag_all("map")
        #Here we draw the player in the center of the screen
        #self.playerImage = C1.create_image(180,180,image = self.player)


        self.fixedUpdate()
    def fixedUpdate(self):

        if self.moveCounter >7:
            self.moveCounter = 0
            if self.mL and self.leftTime>self.rightTime and self.leftTime > self.downTime and self.leftTime> self.upTime:
                print("k")
                try:
                    self.map[self.PY][self.PX - 1].CODE = self.map[self.PY][self.PX - 1].CODE
                except:
                    self.loadSection("-x")

                sceneMove = True
                try:
                    if self.scenery[self.PY][self.PX - 1].CAN_MOVE == False:
                        sceneMove = False
                except:
                    sceneMove = True
                if self.PX <= 0:
                    self.loadSection("-x")
                elif self.map[self.PY][self.PX - 1].CAN_MOVE == True and sceneMove:
                    print("Hi")
                    self.player = self.playerLeft[self.aniCounter]
                    self.aniCounter += 1
                    if self.aniCounter > 3:
                        self.aniCounter = 0

                    self.PX -= 1
                    C1.delete("all")
                    self.updateOnClick()
                    self.draw()


            if self.mR and self.rightTime>self.leftTime and self.rightTime > self.downTime and self.rightTime> self.upTime:

                try:
                    self.map[self.PY][self.PX + 1].CODE = self.map[self.PY][self.PX + 1].CODE
                except:
                    self.loadSection("+x")

                sceneMove = True
                try:
                    if self.scenery[self.PY][self.PX + 1].CAN_MOVE == False:
                        sceneMove = False
                except:
                    sceneMove = True
                if self.PX >= len(self.map[self.PY]) - 1:
                    self.loadSection("+x")
                elif  self.map[self.PY][self.PX + 1].CAN_MOVE == True and sceneMove:
                    self.player = self.playerRight[self.aniCounter]
                    self.aniCounter += 1
                    if self.aniCounter > 3:
                        self.aniCounter = 0
                    self.PX += 1
                    C1.delete("all")
                    self.updateOnClick()
                    self.draw()


            if self.mU and self.upTime>self.leftTime and self.upTime > self.downTime and self.upTime> self.rightTime:

                try:
                    self.map[self.PY - 1][self.PX].CODE = self.map[self.PY - 1][self.PX].CODE
                except:
                    self.loadSection("-y")

                sceneMove = True
                try:
                    if self.scenery[self.PY - 1][self.PX].CAN_MOVE == False:
                        sceneMove = False
                except:
                    sceneMove = True

                if self.PY <= 0:
                    self.loadSection("-y")
                elif  self.map[self.PY - 1][self.PX].CAN_MOVE == True and sceneMove:
                    self.player = self.playerUp[self.aniCounter]
                    self.aniCounter += 1
                    if self.aniCounter > 3:
                        self.aniCounter = 0
                    self.PY -= 1
                    C1.delete("all")
                    self.updateOnClick()
                    self.draw()


            if self.mD and self.downTime>self.leftTime and self.downTime > self.rightTime and self.downTime> self.upTime:

                try:
                    self.map[self.PY + 1][self.PX].CODE = self.map[self.PY + 1][self.PX].CODE
                except:
                    self.loadSection("+y")

                sceneMove = True
                try:
                    if self.scenery[self.PY + 1][self.PX].CAN_MOVE == False:
                        sceneMove = False
                except:
                    sceneMove = True
                if self.PY >= len(self.map) - 1:
                    self.loadSection("+y")

                elif  self.map[self.PY + 1][self.PX].CAN_MOVE == True and sceneMove:

                    self.player = self.playerDown[self.aniCounter]
                    self.aniCounter += 1
                    if self.aniCounter > 3:
                        self.aniCounter = 0
                    self.PY += 1
                    self.updateOnClick()
                    C1.delete("all")
                    self.draw()
        try:
            if self.battle1.battleWon:

                del enemyList[self.enemyToRemove]

                root.bind("<a>", self.onLeftPress)
                root.bind("<d>", self.onRightPress)
                root.bind("<w>", self.onUpPress)
                root.bind("<s>", self.onDownPress)
                root.bind("<KeyRelease-a>", self.onLeftUp)
                root.bind("<KeyRelease-d>", self.onRightUp)
                root.bind("<KeyRelease-s>", self.onDownUp)
                root.bind("<KeyRelease-w>", self.onUpUp)

                root.bind("<Left>", self.onLeftPress)
                root.bind("<Right>", self.onRightPress)
                root.bind("<Up>", self.onUpPress)
                root.bind("<Down>", self.onDownPress)
                root.bind("<z>", self.NPCInteractions)
                root.bind("<KeyRelease-Left>", self.onLeftUp)
                root.bind("<KeyRelease-Right>", self.onRightUp)
                root.bind("<KeyRelease-Down>", self.onDownUp)
                root.bind("<KeyRelease-Up>", self.onUpUp)
        except:
            pass

        self.moveCounter+=1
        root.after(17,self.fixedUpdate)
    def enemyChase(self,enemy):
        for i in range(360):
            ax = math.sin(i)

            ay = math.cos(i)
            x = enemy.x
            y = enemy.y
            for g in range(enemy.chaseRange):
                x += ax
                y += ay
                #print(x)
                if int(round(x)) == self.PX and int(round(y)) == self.PY:
                    enemy.chase = True
                    return i
                else:
                    continue
            #enemy.chasing = False
        return
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


    def updateOnClick(self):
        for i in range(len(enemyList)):
            if abs(enemyList[i].x - self.PX) <= enemyList[i].chaseRange and abs(enemyList[i].y - self.PY) <= enemyList[i].chaseRange:
                y = self.enemyChase(enemyList[i])
                if enemyList[i].chase:
                    if enemyList[i].moveCounter >= 1:
                        try:





                            if int(round(math.sin(y)))== -1:
                                enemyList[i].dir = 3
                                enemyList[i].x += int(round(math.sin(y)))

                            elif int(round(math.sin(y)))== 1:
                                enemyList[i].dir = 1
                                enemyList[i].x += int(round(math.sin(y)))


                            if int(round(math.cos(y))) == -1:
                                enemyList[i].dir = 0
                                enemyList[i].y += int(round(math.cos(y)))

                            elif int(round(math.cos(y))) == 1:
                                enemyList[i].dir = 2
                                enemyList[i].y += int(round(math.cos(y)))


                            print("x" + str(enemyList[i].x),enemyList[i].y)
                        except:

                            continue
                        enemyList[i].moveCounter = 0
                    else:

                        enemyList[i].moveCounter +=1
                    print(enemyList[i].aniCounter)
                    if enemyList[i].dir == 0:
                        enemyList[i].img = enemyList[i].aUp[enemyList[i].aniCounter]
                    elif enemyList[i].dir == 1:
                        enemyList[i].img = enemyList[i].aRight[enemyList[i].aniCounter]
                    elif enemyList[i].dir == 2:
                        enemyList[i].img = enemyList[i].aDown[enemyList[i].aniCounter]
                    elif enemyList[i].dir == 3:
                        enemyList[i].img = enemyList[i].aLeft[enemyList[i].aniCounter]
                    if enemyList[i].aniCounter<=1:
                        enemyList[i].aniCounter += 1
                    elif enemyList[i].aniCounter >= 2:
                        enemyList[i].aniCounter = 0



        for i in range(len(enemyList)):
            if enemyList[i].x == self.PX and enemyList[i].y == self.PY:
                self.enemyToRemove = i
                self.mL = False
                self.mR = False
                self.mU = False
                self.mD = False
                root.unbind("<Left>")
                root.unbind("<Right>")
                root.unbind("<Up>")
                root.unbind("<Down>")
                root.unbind("<z>")
                root.unbind("<KeyRelease-Left>")
                root.unbind("<KeyRelease-Right>")
                root.unbind("<KeyRelease-Down>")
                root.unbind("<KeyRelease-Up>")
                if enemyList[i].type == "FatBat":

                    self.battle1 = binding.Battle(root)
                    eD.FatBat(3)

    def onLeftPress(self,event,*args):
        self.leftTime = event.time
        self.mL = True
    def onRightPress(self,event,*args):
        self.rightTime = event.time
        self.mR = True
    def onUpPress(self,event,*args):
        self.upTime = event.time
        self.mU = True
    def onDownPress(self,event,*args):
        self.downTime = event.time
        self.mD = True
    def onLeftUp(self,*args):
        self.leftTime = 0
        self.mL = False
    def onRightUp(self,*args):
        self.rightTime = 0
        self.mR = False
    def onDownUp(self,*args):
        self.downTime = 0
        self.mD = False
    def onUpUp(self,*args):
        self.upTime = 0
        self.mU = False
    def loadSection(self,dir):
        print("hi")

        #bI.areaList[11][10] = bI.Biome("cave",100,100,True,True,True,True)
        musicChange = False
        C1.delete('all')
        if dir == "+y":
            bI.mapy +=1
            self.PY = 0
            if bI.areaList[bI.mapy][bI.mapx].biome != bI.areaList[bI.mapy-1][bI.mapx].biome:
                bI.areaList[bI.mapy-1][bI.mapx].music.stop()
                musicChange = True
        if dir == "-y":
            bI.mapy -=1
            self.PY = len(bI.areaList[bI.mapy][bI.mapx].map)-1
            if bI.areaList[bI.mapy][bI.mapx].biome != bI.areaList[bI.mapy+1][bI.mapx].biome:
                bI.areaList[bI.mapy+1][bI.mapx].music.stop()
                musicChange = True
        if dir == "+x":
            bI.mapx +=1
            self.PX = 0
            if bI.areaList[bI.mapy][bI.mapx].biome != bI.areaList[bI.mapy][bI.mapx-1].biome:
                bI.areaList[bI.mapy][bI.mapx-1].music.stop()
                musicChange = True
        if dir == "-x":
            bI.mapx -=1
            self.PX = len(bI.areaList[bI.mapy][bI.mapx].map[self.PY//self.tileSize])-1
            if bI.areaList[bI.mapy][bI.mapx].biome != bI.areaList[bI.mapy][bI.mapx+1].biome:
                bI.areaList[bI.mapy][bI.mapx+1].music.stop()
                musicChange = True
        if (musicChange):
            bI.areaList[bI.mapy][bI.mapx].music.play(loops=-1)
        #print(bI.areaList[11][10].biome)
        #print(bI.areaList[11][10].map)
        self.map = bI.areaList[bI.mapy][bI.mapx].map
        self.scenery = bI.areaList[bI.mapy][bI.mapx].scenery
        #for i in range(len(self.map)):
          #  for g in range(len(self.map[i])):
           #     if (self.map[i][g] == "CaveWall-Middle"):
            #        C1.create_image(g*self.tileSize+12-self.PX + 7*self.tileSize,i*self.tileSize+12-self.PY + 7*self.tileSize,image = self.wallImage)
             #   else:
              #      C1.create_image(g*self.tileSize+12-self.PX + 7*self.tileSize,i*self.tileSize+12-self.PY + 7*self.tileSize,image = self.floorImage)
        self.draw()

    def NPCInteractions(self,*args):
        response = eD.eNT(self.PX,self.PY,enemyList)
        if response != "":
            if response == "FatBat":
                print("wow")

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

        print(self.PX,self.PY)
        #print(self.PY-self.DRAWRANGE)
        for y in range((self.PY - self.DRAWRANGE//2), (self.PY + self.DRAWRANGE//2 + 1)):
            xCTR = 0
            for x in range((self.PX - self.DRAWRANGE//2), (self.PX + self.DRAWRANGE//2 + 1)):

                try:
                    #if self.VIEWMAP[y][x] == 0:
                    if x > len(self.map[y]) - 1 or x < 0 or y > len(self.map)-1 or y < 0:
                        xCTR += 1
                        continue
                    else:

                        C1.create_image(xCTR * self.tileSize + 20, yCTR * self.tileSize + 20, image=self.map[y][x].IMAGE_DIR)
                        xCTR += 1
                except:
                    xCTR += 1

            yCTR += 1

        yCTR = 0
        for y in range((self.PY - self.DRAWRANGE // 2), (self.PY + self.DRAWRANGE // 2 + 1)):
            xCTR = 0
            for x in range((self.PX - self.DRAWRANGE // 2), (self.PX + self.DRAWRANGE // 2 + 1)):

                try:
                    if x > len(self.map[y]) - 1 or x < 0 or y > len(self.map)-1 or y < 0:
                        xCTR += 1
                        continue
                    else:
                        C1.create_image(xCTR * self.tileSize+16, yCTR * self.tileSize+16, image=self.scenery[y][x].IMAGE_DIR)
                        try:
                            C1.create_image(xCTR * self.tileSize+16, yCTR * self.tileSize+self.scenery[y][x].OFFSET, image=self.scenery[y][x].IMAGE_SECOND,tags = "treetop")
                        except:
                            pass
                        xCTR +=1
                except:
                    xCTR += 1
                    continue

            yCTR +=1



        for i in range(len(enemyList)):
            #if self.VIEWMAP[enemyList[i].y][enemyList[i].x] == 0:
                #print(enemyList[i].x)
            C1.create_image((enemyList[i].x-self.PX)*self.tileSize + (self.DRAWRANGE//2)*self.tileSize + 20,(enemyList[i].y-self.PY)*self.tileSize + (self.DRAWRANGE//2)*self.tileSize + 20, image = enemyList[i].img)
        C1.create_image((self.mapWidth//2)+4,(self.mapHeight//2),image = self.player)
        C1.tag_raise("treetop")
app = App()
app.run()