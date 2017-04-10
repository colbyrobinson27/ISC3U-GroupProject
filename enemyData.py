import tkinter as tk
import Binding as binding
def eNT(player,list,canvas):
    for i in range(len(list)):
        if abs(canvas.coords(list[i].pos)[0]-canvas.coords(player)[0]) <= 24 and abs(canvas.coords(list[i].pos)[1]-canvas.coords(player)[1]) <=24:
            return list[i].type
        else:
            return ""

class Enemy(object):
    def __init__(self,canvas,type):


        if type == "FatBat":
            self.img = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
            self.pos = canvas.create_image(12,12,image = self.img)
            self.health = 50
            self.damage = 4
            self.type = type
def FatBat():
    binding.Enemy.img = tk.PhotoImage(file="./FatBat.png")
    binding.Enemy.img = binding.Enemy.img.zoom(2, 2)
    binding.Enemy.health = 50
    binding.Enemy.speed = 20.5
    binding.Enemy.speedgain = 0.05
    binding.Enemy.damage = 5
