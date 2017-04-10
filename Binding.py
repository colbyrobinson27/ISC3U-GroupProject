from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import math
import random
import time
from time import gmtime, strftime
root = tk.Tk()
tearlist = []

class Battle():
    def __init__(self):
        global roomc, person
        self.shotspeed = 40
        self.tears = 1
        self.speed =5
        self.damage = 1
        self.luck = 1
        self.knockback = 0.1
        self.size = 16
        self.scale = 40
        self.roomnum = 0
        self.tsize = self.scale*self.size
        self.timer=0
        self.xspeed = 0
        self.yspeed = 0

        self.monsterlist=[]
        self.fatBat = PhotoImage(file="./FatBat.png")
        self.fatBatDamage = PhotoImage(file="./FatBatDamage.png")
        self.imgRight=PhotoImage(file="./WarRight.png")
        self.imgLeft = PhotoImage(file="./WarLeft.png")
        self.imgUp = PhotoImage(file="./WarUp.png")
        self.imgDown = PhotoImage(file="./WarDown.png")

        self.imgDown = self.imgDown.zoom(3, 3)
        self.imgUp = self.imgUp.zoom(3, 3)
        self.imgRight = self.imgRight.zoom(3, 3)
        self.imgLeft = self.imgLeft.zoom(3, 3)
        self.fatBatDamage =self.fatBatDamage.zoom(2,2)
        self.fatBat = self.fatBat.zoom(2,2)
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

        self.monsterlist.append(Enemy(1, self.tsize / 1, self.tsize / 2))
        self.monsterlist.append(Enemy(1, self.tsize / 2, self.tsize / 2))
        self.monsterlist.append(Enemy(1, self.tsize / 3, self.tsize / 2))
        self.monsterlist.append(Enemy(1, self.tsize / 4, self.tsize / 2))

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
            tearlist.append(Tear(self.x-15,self.y-10,-self.shotspeed+self.xspeed,0+self.yspeed,self.tsize))
            self.timer = 0
            roomc.itemconfig(person,image = self.imgLeft)
        if self.shootright == True and self.timer>self.tears:
            tearlist.append(Tear(self.x+15,self.y-10,self.shotspeed+self.xspeed,0+self.yspeed,self.tsize))
            self.timer = 0
            roomc.itemconfig(person, image=self.imgRight)
        if self.shootup == True and self.timer>self.tears:
            tearlist.append(Tear(self.x,self.y,0+self.xspeed,-self.shotspeed+self.yspeed,self.tsize))
            self.timer = 0
            roomc.lift(person)
            roomc.itemconfig(person, image=self.imgUp)
        if self.shootdown == True and self.timer>self.tears:
            tearlist.append(Tear(self.x,self.y,0+self.xspeed,self.shotspeed+self.yspeed,self.tsize))
            self.timer = 0
            roomc.itemconfig(person, image=self.imgDown)

    def returnsprite(self, num):
        roomc.itemconfig(self.monsterlist[num].bat, image=self.fatBat)
        print("nope")

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

            try:

                self.tearx = roomc.coords(tearlist[i].tear)[0]
                self.teary = roomc.coords(tearlist[i].tear)[1]
            except:
                pass
            if self.tearx<38 or self.tearx>self.tsize*2-55 or self.teary>self.tsize-50 or self.teary<38:
                try:
                    roomc.delete(tearlist[i].tear)
                    tearlist.pop(i)
                except:
                    pass
            for j in range(len(self.monsterlist)):

                try:
                    self.bbox = roomc.bbox(self.monsterlist[j].bat)
                except:
                    pass
                if self.tearx>self.bbox[0] and self.tearx<self.bbox[2] and self.teary>self.bbox[1] and self.teary<self.bbox[3]:
                    try:

                        self.monsterlist[j].xspeed = tearlist[i].xspeed * self.knockback
                        self.monsterlist[j].yspeed = tearlist[i].yspeed * self.knockback
                        roomc.delete(tearlist[i].tear)
                        tearlist.pop(i)
                        self.monsterlist[j].hit += 1

                        roomc.itemconfig(self.monsterlist[j].bat, image=self.fatBatDamage)
                        self.monsterlist[j].damagetimer = 0

                        if self.monsterlist[j].hit == self.monsterlist[j].health:
                            roomc.delete(self.monsterlist[j].bat)
                            self.monsterlist.pop(j)


                    except:
                        pass



        for i in range(len(self.monsterlist)-1):
            for k in range((len(self.monsterlist))-1,0,-1):
                if abs(roomc.coords(self.monsterlist[i].bat)[0]-roomc.coords(self.monsterlist[k].bat)[0])<70 and abs(roomc.coords(self.monsterlist[i].bat)[1]-roomc.coords(self.monsterlist[k].bat)[1])<60:
                    if roomc.coords(self.monsterlist[i].bat)[0]>roomc.coords(self.monsterlist[k].bat)[0]:
                        self.monsterlist[i].xspeed = 1
                        self.monsterlist[k].xspeed = -1
                    if roomc.coords(self.monsterlist[i].bat)[0]<roomc.coords(self.monsterlist[k].bat)[0]:
                        self.monsterlist[i].xspeed = -1
                        self.monsterlist[k].xspeed = 1
                    if roomc.coords(self.monsterlist[i].bat)[1] > roomc.coords(self.monsterlist[k].bat)[1]:
                        self.monsterlist[i].yspeed = 1
                        self.monsterlist[k].yspeed = -1
                    if roomc.coords(self.monsterlist[i].bat)[1] < roomc.coords(self.monsterlist[k].bat)[1]:
                        self.monsterlist[i].yspeed = -1
                        self.monsterlist[k].yspeed = 1

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
            self.health =50
            self.speed = 2
            self.speedgain = 0.05
            self.xspeed=self.speed
            self.yspeed = self.speed
            self.damagetimer = 0
            self.hit = 0
            self.update()

    def update(self):
        self.damagetimer+=1
        self.chase()
        self.move()
        if self.damagetimer >4:
            roomc.itemconfig(self.bat, image=self.img)

        root.after(17,self.update)

    def move(self):
        roomc.move(self.bat,self.xspeed,self.yspeed)

    def chase(self):
        self.pos=roomc.coords(self.bat)[0:2]
        self.playerpos = roomc.coords(person)[0:2]
        try:
            if self.pos[0] > self.playerpos[0]:
                self.xspeed+=-self.speedgain
            if self.pos[0] < self.playerpos[0]:
                self.xspeed += self.speedgain
            if self.pos[1] > self.playerpos[1]:
                self.yspeed += -self.speedgain
            if self.pos[1] < self.playerpos[1]:
                self.yspeed += self.speedgain

            if self.xspeed>self.speed:
                self.xspeed=self.speed
            elif self.xspeed<-self.speed:
                self.xspeed=-self.speed
            if self.yspeed>self.speed:
                self.yspeed=self.speed
            elif self.yspeed<-self.speed:
                self.yspeed=-self.speed

        except:
            pass


battle = Battle()
root.mainloop()