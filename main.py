import random
import tkinter as tk
#Hello! This is the home base for operations of the game. The structure below is known as a class, and is where we put all of the things that are in the game.
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
        self.x = 2160
        self.y = 2160
        self.mapx = 10
        self.mapy = 10
        #Here is just variables that are used to stop players from holding down a key and moving extremely fast, not too much to worry about
        self.cMU = True
        self.cMD = True
        self.cMR = True
        self.cML = True
        #These are keybinds. They use tkinter to bind certain keys to certain functions. We have bound all arrow keys on press and on release at the moment
        self.root.bind("<Left>",self.onLeftPress)
        self.root.bind("<Right>",self.onRightPress)
        self.root.bind("<Up>", self.onUpPress)
        self.root.bind("<Down>", self.onDownPress)
        self.root.bind("<KeyRelease-Left>",self.onLeftUp)
        self.root.bind("<KeyRelease-Right>", self.onRightUp)
        self.root.bind("<KeyRelease-Down>", self.onDownUp)
        self.root.bind("<KeyRelease-Up>", self.onUpUp)
        #this is where we import images from the game folder, and assign them to variables
        self.floorImage = tk.PhotoImage(file = ".\GrassFloor1.png")
        self.wallImage = tk.PhotoImage(file = ".\WallSketch5.png")
        self.player = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
        self.areaList = []
        for i in range(50):
            self.areaList.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        #This is the map list; it is where we put all of the 0s and 1s that make up the cave walls and floors
        self.map = []
        #This is the size of the map, it is used for all kinds of calculations and for generating the map
        self.mapsize = 100
        self.map = self.generateCave(self.mapsize)
        self.areaList[10][10] = self.map
        #This forloor draws everything that is in the self.map variable to the screen (tk.C1). It uses a camera offset of 7 x and 7 y tiles in order to set the players position onscreen equal to the self.x and self.y variables
        for i in range(self.mapsize):
            for g in range(self.mapsize):
                if (self.map[i][g] == "CaveWall-Middle"):
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.wallImage)
                else:
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.floorImage)
        #We tag all of the pieces of the map as "map" now so that we can move them all without moving the player, as instead of moving a player and having to redraw the screen
        #we can simply move the tiles around the player to give semblence of movement
        self.C1.addtag_all("map")
        #Here we draw the player in the center of the screen
        self.C1.create_image(180,180,image = self.player)
        self.timer_tick()
    def run(self):
        self.root.mainloop()
    def generateCave(self,size):
        map = []
        # This forloop adds enough lists to our map lists for all the Xs and Ys of the map. This creates a 2 dimensional list thats variables can be accessed by typing self.map[y][x]
        # outside of this function, or map[y][x] inside of the function. This is how we easily set up a 2d world
        for i in range(size):
            map.append([])
            #This loop randomly adds a floor of wall to the embedded lists
            for g in range(size):

                #This gives the game walls with 40% probability and floors with 60% so we decrease the fill percentage in order to create a flowing cave environment
                if random.randint(0,4)//3 == 0:
                    #Throughout the project we will be using names for tiles as seen below
                    map[i].append("CaveWall-Middle")
                else:
                    map[i].append("Grass-Dark")
        #this is the first of 2 procedures to generate the caves. Logic is make it a floor if 5 or more in 1 distance of tile are floors or there re no floors within 2 distance of floor, with a few minor if statements that give tweaks and flow to the
        #cave system
        for h in range(4):
            for i in range(size):
                for g in range(size):
                    #print(g)

                    if self.nextTo2(1,map,g,i,"Grass-Dark") >=5 or self.nextTo2(2,map,g,i,"Grass-Dark") <=2:
                        map[i][g] = "Grass-Dark"
                        #minor change, maks it a wall if there are less than 3 grass tiles within 1 area
                    elif self.nextTo2(1,map,g,i,"Grass-Dark") <=2:
                        map[i][g] = "CaveWall-Middle"
        #Second procedure, logic is the same as the first except without setting it to a floor if there are no floors within 2 distance. This time however we set all tiles that arent being set to a floor to a wall
        for h in range(3):
            for i in range(size):
                for g in range(size):
                    # print(g)

                    if self.nextTo2(1, map, g, i, "Grass-Dark") >= 5:
                        map[i][g] = "Grass-Dark"
                    else:
                        map[i][g] = "CaveWall-Middle"
        #This sets all the borders of the map to walls so that for the time being the player cannot wander off the side of the map
        #for i in range(size):
         #   for g in range(size):
                #or i == size-1
          #      if i ==0  or g == 0 or g == size-1:
           #         map[i][g] = "CaveWall-Middle"
        print(map[99])

        #This section only serves to print the entire map line by line to the console, is only useful for debugging and will be removed when the game is finished
        curstring = ""
        for i in range(size):

            curstring = ""
            for g in range(size):
                if map[i][g] == "CaveWall-Middle":

                    curstring += "#"
                else:
                    curstring += "."
            print(curstring)
        return map
    def timer_tick(self):


        self.root.after(50,self.timer_tick)
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
    def nextTo2(self,scale,list,x,y,n):
        ans = 0
        for i in range(-scale,scale+1,1):
            for g in range(-scale,scale+1,1):
                if x + g >= 0 and x + g <= self.mapsize-1 and y + i >= 0 and y + i <= self.mapsize-1 and list[y+i][x+g] == n:

                    ans += 1
        return ans


    def onLeftPress(self,*args):
        if self.x <= 0:
            self.loadSection("-x")
        elif self.cML and self.map[self.y//24][(self.x-24)//24] != "CaveWall-Middle":
                self.C1.move("map", 24, 0)
                self.x -= 24
        self.cML = False

    def onRightPress(self,*args):
        if self.x >= - 24 + self.mapsize * 24:
            self.loadSection("+x")
        if self.cMR and self.map[self.y//24][(self.x+24)//24] != "CaveWall-Middle":
                self.C1.move("map", -24, 0)
                self.x += 24
        self.cMR = False
    def onUpPress(self,*args):
        if self.y <= 0:
            self.loadSection("-y")
        elif self.cMU and self.map[(self.y-24)//24][self.x//24] != "CaveWall-Middle":
                self.C1.move("map", 0, 24)
                self.y -= 24
        self.cMU = False
    def onDownPress(self,*args):
        #print((self.y+24)//24,self.x//24)
        if self.y >=  - 24 + self.mapsize * 24:
            self.loadSection("+y")
        elif self.cMD and self.map[(self.y+24)//24][self.x//24] != "CaveWall-Middle":
                self.C1.move("map", 0, -24)
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
        self.areaList[11][10] = self.generateCave(100)

        self.C1.delete('all')
        if dir == "+y":
            self.mapy +=1

        if dir == "-y":
            self.mapy -=1

        if dir == "+x":
            self.mapx +=1

        if dir == "-x":
            self.map -=1
        self.map = self.areaList[self.mapy][self.mapx]
        for i in range(self.mapsize):
            for g in range(self.mapsize):
                if (self.map[i][g] == "CaveWall-Middle"):
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.wallImage)
                else:
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.floorImage)

app = App()
app.run()