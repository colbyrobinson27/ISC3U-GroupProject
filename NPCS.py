import tkinter as tk
import NameGenerator as nameGen
class NPC():
    def __init__(self,package):
        self.img = tk.PhotoImage(file = "./Images/NPC/" + package[0] + "/down1.png")
        self.x = 0
        self.y = 0
        self.type = package[1]
        self.name = nameGen.characterNameGenerator()

npcBase = [["NPC01","shop"]]