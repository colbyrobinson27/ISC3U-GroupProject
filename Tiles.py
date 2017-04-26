import tkinter as tk
class Tile:
    def __init__(self,NAME,CAN_SEE,CAN_MOVE,IMAGE_DIR,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file = IMAGE_DIR)
        self.CODE = CODE
        self.NAME = NAME
caveFloor = Tile("caveFloor",True,True,".\\rockfloor1.png",0)
caveWall = Tile("caveWall",False,False,".\cavewall1.png",1)
grass1 = Tile("grass1",True,True,".\grass1.png",2)
desert1 = Tile("desert1",True,True,".\desert1.png",3)
tileSet = [caveWall,caveFloor,grass1,desert1]
class Scenery:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,IMAGE_SECOND,YOFFSET,XOFFSET,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file=IMAGE_DIR)
        self.YOFFSET = YOFFSET
        self.XOFFSET = XOFFSET
        try:
            self.IMAGE_SECOND = tk.PhotoImage(file =IMAGE_SECOND)
        except:
            pass
        self.CODE = CODE
tree1 = Scenery(True,False,"./treebot.png","./treetop.png",-32,0,1)
#stag1 = Scenery(True,False,"./Images/Scenery/StagBot.png", "./Images/Scenery/StagTop.png",-16,2)
cactus1 = Scenery(True,False,"./cactus1Bottom.png","./cactus1Top.png",-15,0,3)
rock1 = Scenery(True,False,"./RockBot1.png","./RockTop1.png",-5,0,2)
caveWallB = Scenery(True,False,"./Images/Scenery/CaveWallB1.png","./Images/Scenery/CaveWallB2.png",-16,4,4)
scenerySet = [tree1,rock1,cactus1,caveWallB]
