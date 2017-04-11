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
            self.pos = canvas.create_image(1,1,image = self.img)
            self.health = 50
            self.damage = 4
            self.type = type

def FatBat(num):
    for i in range(num):
            enemylist = []
            enemylist.append(binding.Enemy(1,50,50))
            enemylist[i].img = tk.PhotoImage(file="./FatBat.png")
            enemylist[i].img = enemylist[i].img.zoom(2, 2)
            enemylist[i].health = 1
            enemylist[i].speed = 3
            enemylist[i].speedgain = 0.05
            enemylist[i].damage = 5

