import random
class Biome():
    def __init__(self,type,x,y):
        self.map = []
        self.x = x
        self.y = y
        self.hostility = 0
        if type == "cave":
            self.map = self.generateCave()
            #self.hostility = 2
            self.biome = "cave"
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
                        # for i in range(size):
                        #   for g in range(size):
                        # or i == size-1
                        #      if i ==0  or g == 0 or g == size-1:
                        #         map[i][g] = "CaveWall-Middle"
        print(map[99])

        # This section o the entire map line by line to the console, is only useful for debugging and will be removed when the game is finished

        return map
    def nextTo2(self,scale,list,x,y,n):
        ans = 0
        for i in range(-scale,scale+1,1):
            for g in range(-scale,scale+1,1):
                if x + g >= 0 and x + g <= self.x-1 and y + i >= 0 and y + i <= self.y-1 and list[y+i][x+g] == n:

                    ans += 1
        return ans