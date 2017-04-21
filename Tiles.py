import tkinter as tk
class Tile:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file = IMAGE_DIR)
        self.CODE = CODE
caveFloor = Tile(True,True,".\\rockfloor1.png",0)
caveWall = Tile(False,False,".\cavewall1.png",1)
grass1 = Tile(True,True,".\grass1.png",2)
desert1 = Tile(True,True,".\desert1.png",3)
tileSet = [caveWall,caveFloor,grass1,desert1]
class Scenery:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,IMAGE_SECOND,OFFSET,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file=IMAGE_DIR)
        self.OFFSET = OFFSET
        try:
            self.IMAGE_SECOND = tk.PhotoImage(file =IMAGE_SECOND)
        except:
            pass
        self.CODE = CODE
tree1 = Scenery(True,False,"./treebot.png","./treetop.png",-32,1)
stag1 = Scenery(True,False,"./Images/Scenery/StagBot.png", "./Images/Scenery/StagTop.png",-16,2)
cactus1 = Scenery(True,False,"./cactus1Bottom.png","./cactus1Top.png",-16,3)
scenerySet = [tree1,stag1,cactus1]
