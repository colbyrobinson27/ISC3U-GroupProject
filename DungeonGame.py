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
        self.x = 216
        self.y = 216
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
        #This is the map list; it is where we put all of the 0s and 1s that make up the cave walls and floors
        self.map = []
        #This is the size of the map, it is used for all kinds of calculations and for generating the map
        self.mapsize = 100
        #This forloop adds enough lists to our map lists for all the Xs and Ys of the map. This creates a 2 dimensional list thats variables can be accessed by typing self.mapsize[y][x]. This is how we easily set up a 2d world
        for i in range(self.mapsize):
            self.map.append([])
            #This loop randomly adds a 1(floor) or 0 (wall) to the embedded lists
            for g in range(self.mapsize):

                self.map[i].append(random.randint(0, 1))

        for h in range(5):
            for i in range(self.mapsize):
                for g in range(self.mapsize):
                    #print(g)
                    if self.map[i][g] == 1:
                        if self.nextTo(self.map,g,i,1) >=4 :
                            self.map[i][g] = 1
                        else:
                            self.map[i][g] = 0
                    else:
                        if self.nextTo(self.map,g,i,1) >= 5:
                            self.map[i][g] = 1



        curstring = ""
        for i in range(self.mapsize):
            print(curstring)
            curstring = ""
            for g in range(self.mapsize):
                if self.map[i][g] == 0:

                    curstring += "#"
                else:
                    curstring += "."
        print("\n" + str(self.nextTo(self.map,0,0,0)))
        for i in range(self.mapsize):
            for g in range(self.mapsize):
                if (self.map[i][g] == 0):
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.wallImage)
                else:
                    self.C1.create_image(g*24+12-self.x + 7*24,i*24+12-self.y + 7*24,image = self.floorImage)
        self.C1.addtag_all("map")
        self.C1.create_image(180,180,image = self.player)
        self.timer_tick()
    def run(self):
        self.root.mainloop()
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
        for i in range(-scale,scale+1,1):
            for g in range(-scale,scale+1,1):
                if x + g >= 0 and x + g <= self.mapsize-1 and y + i >= 0 and y + i <= self.mapsize-1:


    def onLeftPress(self,*args):

        if self.cML and self.x >=24 and self.map[self.y//24][(self.x-24)//24] != 0:
            self.C1.move("map", 24, 0)
            self.x -= 24
        self.cML = False

    def onRightPress(self,*args):
        if self.cMR and self.x <= self.mapsize*24-24 and self.map[self.y//24][(self.x+24)//24] != 0:
            self.C1.move("map", -24, 0)
            self.x += 24
        self.cMR = False
    def onUpPress(self,*args):
        if self.cMU and self.y >=24 and self.map[(self.y-24)//24][self.x//24] != 0:
            self.C1.move("map", 0, 24)
            self.y -= 24
        self.cMU = False
    def onDownPress(self,*args):
        #print((self.y+24)//24,self.x//24)
        if self.cMD and self.y <= self.mapsize*24-24 and self.map[(self.y+24)//24][self.x//24] != 0:
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

app = App()
app.run()