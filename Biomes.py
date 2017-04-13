import random
areaList = []
mapx = 10
mapy = 10
for i in range(50):
    areaList.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
class Biome():
    def __init__(self,type,x,y,left,right,top,bottom,xpos,ypos):

        self.map = []
        self.x = x
        self.y = y
        self.left = left
        self.bottom = bottom
        self.top = top
        self.right = right
        self.hostility = 0
        self.integrated = False

        self.biome = ""
        if type == "cave":
            self.map = self.generateCave()
            #self.hostility = 2
            self.biome = "cave"


        try:

            print(areaList[ypos-1][xpos].biome)
            if areaList[ypos-1][xpos].biome == "cave" and areaList[ypos-1][xpos].bottom:
                #print("anywhere pls")
                self.map.reverse()
                self.map.append(areaList[ypos-1][xpos].map[areaList[ypos-1][xpos].y - 1])
                self.map.reverse()
        except:
            print("nonExistent")
        try:
            if areaList[ypos+1][xpos].biome == "cave" and areaList[ypos+1][xpos].top:
                self.map.reverse()
                #print("well we made it...")
                self.map.append(areaList[ypos+1][xpos].map[0])
                self.map.reverse()
        except:
            print("nonExistent")
        try:
            if areaList[ypos][xpos+1].biome == "cave" and areaList[ypos][xpos+1].left:
                if len(areaList[ypos][xpos+1].map) > len(self.map):

                    for i in range(len(areaList[ypos][xpos+1].map) - len(self.map)):
                        self.map.append([])

                for i in range(len(areaList[ypos][xpos+1].map)):
                    self.map[i].reverse()
                    self.map[i].append(areaList[ypos][xpos+1].map[i][0])
                    self.map[i].reverse()


        except:
            print("nonExistent")
        try:
            if areaList[ypos][xpos - 1].biome == "cave" and areaList[ypos][xpos - 1].right:
                if len(areaList[ypos][xpos -1].map) > len(self.map):
                    for i in range(len(areaList[ypos][xpos -1].map) - len(self.map)):
                        self.map.append([])

                for i in range(len(areaList[ypos][xpos -1].map)):

                    self.map[i].append(areaList[ypos][xpos - 1].map[i][len(areaList[ypos][xpos+1].map[i])-1])

        except:
            print("nonExistent")
    def generateCave(self):
        map = []
        # This forloop adds enough lists to our map lists for all the Xs and Ys of the map. This creates a 2 dimensional list thats variables can be accessed by typing self.map[y][x]
        # outside of this function, or map[y][x] inside of the function. This is how we easily set up a 2d world
        for i in range(self.y):
            map.append([])
            # This loop randomly adds a floor of wall to the embedded lists
            for g in range(self.x):

                # This gives the game walls with 40% probability and floors with 60% so we decrease the fill percentage in order to create a flowing cave environment
                if random.randint(0, 4) // 3 == 0:
                    # Throughout the project we will be using names for tiles as seen below
                    map[i].append("CaveWall-Middle")
                else:
                    map[i].append("Grass-Dark")
        # this is the first of 2 procedures to generate the caves. Logic is make it a floor if 5 or more in 1 distance of tile are floors or there re no floors within 2 distance of floor, with a few minor if statements that give tweaks and flow to the
        # cave system
        for h in range(4):
            for i in range(self.y):
                for g in range(self.x):
                    # print(g)

                    if self.nextTo2(1, map, g, i, "Grass-Dark") >= 5 or self.nextTo2(2, map, g, i,
                                                                                     "Grass-Dark") <= 2:
                        map[i][g] = "Grass-Dark"
                        # minor change, maks it a wall if there are less than 3 grass tiles within 1 area
                    elif self.nextTo2(1, map, g, i, "Grass-Dark") <= 2:
                        map[i][g] = "CaveWall-Middle"
        # Second procedure, logic is the same as the first except without setting it to a floor if there are no floors within 2 distance. This time however we set all tiles that arent being set to a floor to a wall
        for h in range(3):
            for i in range(self.y):
                for g in range(self.x):
                    # print(g)

                    if self.nextTo2(1, map, g, i, "Grass-Dark") >= 5:
                        map[i][g] = "Grass-Dark"
                    else:
                        map[i][g] = "CaveWall-Middle"
                        # This sets all the borders of the map to walls so that for the time being the player cannot wander off the side of the map
        if self.left != True:
            for i in range(self.y):
                map[i][0] = "CaveWall-Middle"


        if self.right != True:
            for i in range(self.y):
                map[i][self.x-1] = "CaveWall-Middle"
        if self.bottom != True:
            for i in range(self.x):
                map[self.y-1][i] = "CaveWall-Middle"
        if self.top != True:
            for i in range(self.x):
                map[0][i] = "CaveWall-Middle"
        for i in range(self.y):

            curstring = ""
            for g in range(self.x):
                if map[i][g] == "CaveWall-Middle":

                    curstring += "#"
                else:
                    curstring += "."
            #print(curstring)
        #print(map[99])

        # This section o the entire map line by line to the console, is only useful for debugging and will be removed when the game is finished

        return map
    def nextTo2(self,scale,list,x,y,n):
        ans = 0
        for i in range(-scale,scale+1,1):
            for g in range(-scale,scale+1,1):
                if x + g >= 0 and x + g <= self.x-1 and y + i >= 0 and y + i <= self.y-1 and list[y+i][x+g] == n:

                    ans += 1
        return ans
def createSegment(type,xsize,ysize,left,right,top,bottom,x,y):
    areaList[y][x] = Biome(type,xsize,ysize,left,right,top,bottom,x,y)
