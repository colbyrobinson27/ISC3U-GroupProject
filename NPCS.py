import tkinter as tk
class NPC():
    def __init__(self,package):
        self.img = tk.PhotoImage(file = "./Images/NPC/" + package[0] + "/down1.png")
        self.x = 0
        self.y = 0
        self.type = package[1]

npcBase = [["NPC01","shop"]]