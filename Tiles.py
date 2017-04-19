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
tileSet = [caveWall,caveFloor,grass1]
class Scenery:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file=IMAGE_DIR)
        self.CODE = CODE
tree1 = Scenery(True,False,".\\tree1.png",1)
scenerySet = [tree1]
