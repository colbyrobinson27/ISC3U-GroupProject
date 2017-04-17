import tkinter as tk
class Tile:
    def __init__(self,CAN_SEE,CAN_MOVE,IMAGE_DIR,CODE):
        self.CAN_SEE = CAN_SEE
        self.CAN_MOVE = CAN_MOVE
        self.IMAGE_DIR = tk.PhotoImage(file = IMAGE_DIR)
        self.CODE = CODE
caveFloor = Tile(True,True,".\GrassFloor1.png",0)
caveWall = Tile(False,False,".\WallSketch5.png",1)
tileSet = [caveWall,caveFloor]
