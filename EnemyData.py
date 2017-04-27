import tkinter as tk
import Binding as binding
import random
def eNT(x,y,list):

    for i in range(len(list)):

        if abs(x-list[i].x) <= 1 and abs(y-list[i].y) <=1:
            return list[i].type
        else:
            continue
    return ""
enemypositionsx = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
enemypositionsy = [50,100,150,200,250,300,350,400,450,500,550,600]
class Enemy(object):
    def __init__(self,package):

        self.type = package[0]

        self.img = tk.PhotoImage(file = "./Images/Enemies/" +package[1] +"/" + package[1] + "Down1.png")
        #self.pos = canvas.create_image(x,y,image = self.img)

        self.x = 0
        self.y = 0
        self.chaseRange = package[2]
        self.chase = False
        self.moveCounter = 0
        self.aniCounter = 0
        self.batDown1 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Down1.png")
        self.batDown2 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Down2.png")
        self.batDown3 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Down3.png")
        self.batUp1 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Up1.png")
        self.batUp2 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Up2.png")
        self.batUp3 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Up3.png")
        self.batRight1 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Right1.png")
        self.batRight2 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Right2.png")
        self.batRight3 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Right3.png")
        self.batLeft1 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Left1.png")
        self.batLeft2 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Left2.png")
        self.batLeft3 = tk.PhotoImage(file="./Images/Enemies/" +package[1] +"/" + package[1] + "Left3.png")
        self.dir = 2

        self.aLeft = [self.batLeft1, self.batLeft2, self.batLeft3]
        self.aRight = [self.batRight1, self.batRight2, self.batRight3]
        self.aDown = [self.batDown1,self.batDown2,self.batDown3]
        self.aUp = [self.batUp1,self.batUp2,self.batUp3]



def FatBat(num):
    for i in range(num):
            binding.monsterlist.append(binding.Enemy(enemypositionsx[random.randint(0,22)],enemypositionsy[random.randint(0,10)]))
            binding.monsterlist[i].img = tk.PhotoImage(file="./FatBat.png")
            binding.monsterlist[i].img = binding.monsterlist[i].img.zoom(2, 2)
            binding.monsterlist[i].health = 3
            binding.monsterlist[i].speed = 3
            binding.monsterlist[i].speedgain = 0.05
            binding.monsterlist[i].damage = 5

enemyDict = {
    "fatbat": FatBat
}