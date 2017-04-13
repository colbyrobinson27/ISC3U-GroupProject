import tkinter as tk
import Binding as binding
import random
def eNT(player,list,canvas):
    for i in range(len(list)):
        if abs(canvas.coords(list[i].pos)[0]-canvas.coords(player)[0]) <= 24 and abs(canvas.coords(list[i].pos)[1]-canvas.coords(player)[1]) <=24:
            return list[i].type
        else:
            return ""
enemypositionsx = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
enemypositionsy = [50,100,150,200,250,300,350,400,450,500,550,600]
class Enemy(object):
    def __init__(self,canvas,type):


        if type == "FatBat":
            self.img = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
            self.pos = canvas.create_image(180,180,image = self.img)
            self.type = type

def FatBat(num):
    for i in range(num):
            binding.monsterlist.append(binding.Enemy(enemypositionsx[random.randint(0,22)],enemypositionsy[random.randint(0,10)]))
            binding.monsterlist[i].img = tk.PhotoImage(file="./FatBat.png")
            binding.monsterlist[i].img = binding.monsterlist[i].img.zoom(2, 2)
            binding.monsterlist[i].health = 3
            binding.monsterlist[i].speed = 3
            binding.monsterlist[i].speedgain = 0.05
            binding.monsterlist[i].damage = 5

