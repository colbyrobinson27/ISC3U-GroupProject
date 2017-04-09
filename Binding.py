from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import math
import random
from time import gmtime, strftime
root = tk.Tk()
tearlist = []
monsterlist = []
class Battle():
    def __init__(self):
        global roomc, person
        self.shotspeed = 3.2
        self.tears = 40
        self.speed = 3
        self.damage = 1
        self.luck = 1
        self.size = 16
        self.scale = 40
        self.roomnum = 0
        self.tsize = self.scale*self.size
        self.timer=0
        self.xspeed = 0
        self.yspeed = 0


        self.imgRight=PhotoImage(file="./WarRight.png")
        self.imgLeft = PhotoImage(file="./WarLeft.png")
        self.imgUp = PhotoImage(file="./WarUp.png")
        self.imgDown = PhotoImage(file="./WarDown.png")

        self.imgDown = self.imgDown.zoom(3, 3)
        self.imgUp = self.imgUp.zoom(3, 3)
        self.imgRight = self.imgRight.zoom(3, 3)
        self.imgLeft = self.imgLeft.zoom(3, 3)
        self.floorimg = PhotoImage(file="./floor.png")
        self.floorimg=self.floorimg.zoom(2,1)
        root.config(width=self.tsize*2,height = self.tsize)
        roomc=Canvas(width=self.tsize*2,height=self.tsize,bg="#9e570c")
        roomc.pack()
        roomc.create_image(self.tsize,self.tsize/2,image=self.floorimg)
        person = roomc.create_image(self.tsize,self.tsize/2,image = self.imgDown)


        self.shootleft=False
        self.shootright=False
        self.shootdown=False
        self.shootup=False

        self.a = False
        self.d = False
        self.s = False
        self.w = False

        root.bind("<a>", self.adef)
        root.bind("<w>", self.wdef)
        root.bind("<s>", self.sdef)
        root.bind("<d>", self.ddef)
        root.bind("<KeyRelease-a>", self.aup)
        root.bind("<KeyRelease-d>", self.dup)
        root.bind("<KeyRelease-w>", self.wup)
        root.bind("<KeyRelease-s>", self.sup)
        root.bind("<Left>",self.left)
        root.bind("<Up>", self.up)
        root.bind("<Down>", self.down)
        root.bind("<Right>", self.right)
        root.bind("<KeyRelease-Left>",self.leftup)
        root.bind("<KeyRelease-Right>", self.rightup)
        root.bind("<KeyRelease-Up>", self.upup)
        root.bind("<KeyRelease-Down>", self.downup)
        self.update()
        self.shoot()

    def aup(self,*args):
        self.a = False
        self.xspeed=0
    def dup(self,*args):
        self.d = False
        self.xspeed=0
    def wup(self,*args):
        self.w = False
        self.yspeed=0
    def sup(self,*args):
        self.s = False
        self.yspeed=0
    def ddef(self,*args):
        self.d = True
    def adef(self,*args):
        self.a = True
    def wdef(self,*args):
        self.w = True
    def sdef(self,*args):
        self.s = True

    def move(self,*args):
        if self.d == True:
            roomc.move(person,self.speed,0)
            self.xspeed = self.speed/2
            self.yspeed = 0
        if self.s == True:
            roomc.move(person,0,self.speed)
            self.xspeed = 0
            self.yspeed = self.speed/2
        if self.a == True:
            roomc.move(person,-self.speed,0)
            self.xspeed = -self.speed/2
            self.yspeed = 0
        if self.w == True:
            roomc.move(person,0,-self.speed)
            self.xspeed = 0
            self.yspeed = -self.speed/2

    def leftup(self,*args):
        self.shootleft = False
    def rightup(self,*args):
        self.shootright = False
    def upup(self,*args):
        self.shootup = False
    def downup(self,*args):
        self.shootdown = False

    def right(self,*args):
        self.shootright = True
    def left(self,*args):
        self.shootleft = True
    def up(self,*args):
        self.shootup = True
    def down(self,*args):
        self.shootdown = True

    def shoot(self):
        if self.shootleft == True and self.timer>self.tears:
            Tear(self.x-15,self.y-10,-self.shotspeed+self.xspeed,0+self.yspeed,self.tsize)
            self.timer = 0
            roomc.itemconfig(person,image = self.imgLeft)
        if self.shootright == True and self.timer>self.tears:
            Tear(self.x+15,self.y-10,self.shotspeed+self.xspeed,0+self.yspeed,self.tsize)
            self.timer = 0
            roomc.itemconfig(person, image=self.imgRight)
        if self.shootup == True and self.timer>self.tears:
            Tear(self.x,self.y,0+self.xspeed,-self.shotspeed+self.yspeed,self.tsize)
            self.timer = 0
            roomc.lift(person)
            roomc.itemconfig(person, image=self.imgUp)
        if self.shootdown == True and self.timer>self.tears:
            Tear(self.x,self.y,0+self.xspeed,self.shotspeed+self.yspeed,self.tsize)
            self.timer = 0
            roomc.itemconfig(person, image=self.imgDown)

    def collision(self):
        if roomc.coords(person)[0] < 40:
            roomc.move(person,self.speed,0)
        if roomc.coords(person)[0] >self.tsize*2- 60:
            roomc.move(person,-self.speed,0)
        if roomc.coords(person)[1] < 40:
            roomc.move(person,0,self.speed)
        if roomc.coords(person)[1]+40 > self.tsize-40:
            roomc.move(person,0,-self.speed)
        for i in range(len(tearlist)):
            print(tearlist)
            try:

                self.tearx = roomc.coords(tearlist[i])[0]
                self.teary = roomc.coords(tearlist[i])[1]
            except:
                pass
            if self.tearx<38 or self.tearx>self.tsize*2-55 or self.teary>self.tsize-50 or self.teary<38:
                try:
                    roomc.delete(tearlist[i])
                    tearlist.pop(i)
                except:
                    pass
            for j in range(len(monsterlist)):
                try:
                    self.bbox = roomc.bbox(monsterlist[j])
                except:
                    pass
                if self.tearx>self.bbox[0] and self.tearx<self.bbox[2] and self.teary>self.bbox[1] and self.teary<self.bbox[3]:
                    try:
                        roomc.delete(tearlist[i])
                        tearlist.pop(i)
                        roomc.delete(monsterlist[j])
                        monsterlist.pop(j)
                    except:
                        pass
        for i in range(len(monsterlist)//2):
            for k in range(len(monsterlist)//2,len(monsterlist)):
                if abs(roomc.coords(monsterlist[i])[0]-roomc.coords(monsterlist[k])[0])<70 and abs(roomc.coords(monsterlist[i])[1]-roomc.coords(monsterlist[k])[1])<60:
                    if roomc.coords(monsterlist[i])[0]>roomc.coords(monsterlist[k])[0]:
                        roomc.move(monsterlist[i],1,0)
                        roomc.move(monsterlist[k],-1,0)
                    if roomc.coords(monsterlist[i])[0]<roomc.coords(monsterlist[k])[0]:
                        roomc.move(monsterlist[i],-10,0)
                        roomc.move(monsterlist[k],10,0)
                    if roomc.coords(monsterlist[i])[1] > roomc.coords(monsterlist[k])[1]:
                        roomc.move(monsterlist[i], 0, 1)
                        roomc.move(monsterlist[k], 0, -1)
                    if roomc.coords(monsterlist[i])[1] < roomc.coords(monsterlist[k])[1]:
                        roomc.move(monsterlist[i], 0, -1)
                        roomc.move(monsterlist[k], 0, 1)

    def update(self):
        self.move()
        self.shoot()
        self.collision()
        self.x = roomc.coords(person)[0]-10
        self.y = roomc.coords(person)[1]-10
        self.timer+=1
        root.after(17,self.update)



class Tear():
    def __init__(self,x,y,xspeed,yspeed,tsize):
        self.damage = 1
        self.size = 20
        self.tsize = tsize
        self.tear=roomc.create_oval(x,y,x+self.size,y+self.size,fill="#70e4ff")
        tearlist.append(self.tear)
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.update()

    def update(self):
        self.move()
        root.after(17,self.update)
    def move(self):
        roomc.move(self.tear,self.xspeed,self.yspeed)


class Enemy:
    def __init__(self,num,x,y):
        if num ==1: #FatBat
            self.img = PhotoImage(file = "./FatBat.png")
            self.img=self.img.zoom(2,2)
            self.bat = roomc.create_image(x,y,image=self.img)
            monsterlist.append(self.bat)
            self.health =4
            self.speed = 1
            self.update()

    def update(self):
        self.chase()

        root.after(17,self.update)

    def chase(self):
        self.pos=roomc.coords(self.bat)[0:2]
        self.playerpos = roomc.coords(person)[0:2]
        try:
            if self.pos[0] > self.playerpos[0]:
                roomc.move(self.bat,-self.speed,0)
            if self.pos[0] < self.playerpos[0]:
                roomc.move(self.bat,self.speed,0)
            if self.pos[1] > self.playerpos[1]:
                roomc.move(self.bat,0,-self.speed)
            if self.pos[1] < self.playerpos[1]:
                roomc.move(self.bat,0,self.speed)
        except:
            pass

def bounce(distance, time,canvas,object):
    canvas.move(object)
battle = Battle()
bat =Enemy(1,500,250)
bat2 =Enemy(1,450,100)
root.mainloop()