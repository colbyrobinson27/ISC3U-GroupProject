from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import math
import random



class Player():
    def __init__(self,char):
        if char == "warrior":
            self.health = 5
            self.damage = 1.3
            self.luck = 1
            self.armour = 0

class Battle():
    def __init__(self,root):
        global root1, tearlist, monsterlist
        root1 = root
        tearlist = []
        global roomc, person
        self.shotspeed = 5
        self.tears = 40
        self.speed =5
        self.damage = 1
        self.luck = 1
        self.knockback = 0.05
        self.size = 16
        self.scale = 40
        self.roomnum = 0
        self.tsize = self.scale*self.size
        self.timer=0
        self.xspeed = 0
        self.yspeed = 0
        self.health = 100
        self.damagetimer=0
        monsterlist=[]
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
        root1.config(width=self.tsize*2,height = self.tsize+80)
        roomc=Canvas(root1)

        roomc.pack()
        roomc.config(width=self.tsize * 2, height=self.tsize+80)
        roomc.create_image(self.tsize,self.tsize/2,image=self.floorimg)
        person = roomc.create_image(self.tsize,self.tsize/2,image = self.imgDown)

        self.healthbar = roomc.create_rectangle(100,self.tsize+25,self.health*3+100,self.tsize+55,fill = "green")
        self.healthLabel = Label(text="Health", font = ("papyrus",15))
        self.healthLabel.place(x=30,y=self.tsize+25)
        self.shootleft=False
        self.shootright=False
        self.shootdown=False
        self.shootup=False

        self.a = False
        self.d = False
        self.s = False
        self.w = False

        root1.bind("<a>", self.adef)
        root1.bind("<w>", self.wdef)
        root1.bind("<s>", self.sdef)
        root1.bind("<d>", self.ddef)
        root1.bind("<KeyRelease-a>", self.aup)
        root1.bind("<KeyRelease-d>", self.dup)
        root1.bind("<KeyRelease-w>", self.wup)
        root1.bind("<KeyRelease-s>", self.sup)
        root1.bind("<Left>",self.left)
        root1.bind("<Up>", self.up)
        root1.bind("<Down>", self.down)
        root1.bind("<Right>", self.right)
        root1.bind("<KeyRelease-Left>",self.leftup)
        root1.bind("<KeyRelease-Right>", self.rightup)
        root1.bind("<KeyRelease-Up>", self.upup)
        root1.bind("<KeyRelease-Down>", self.downup)


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
            self.xspeed = self.speed/5
            self.yspeed = 0
        if self.s == True:
            roomc.move(person,0,self.speed)
            self.xspeed = 0
            self.yspeed = self.speed/5
        if self.a == True:
            roomc.move(person,-self.speed,0)
            self.xspeed = -self.speed/5
            self.yspeed = 0
        if self.w == True:
            roomc.move(person,0,-self.speed)
            self.xspeed = 0
            self.yspeed = -self.speed/5


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
        roomc.itemconfig(monsterlist[num].bat, image=self.fatBat)
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
            for j in range(len(monsterlist)):

                try:
                    self.bbox = roomc.bbox(monsterlist[j].bat)
                except:
                    pass
                if self.tearx>self.bbox[0] and self.tearx<self.bbox[2] and self.teary>self.bbox[1] and self.teary<self.bbox[3]:
                    try:

                        monsterlist[j].xspeed = tearlist[i].xspeed * self.knockback
                        monsterlist[j].yspeed = tearlist[i].yspeed * self.knockback
                        roomc.delete(tearlist[i].tear)
                        tearlist.pop(i)
                        monsterlist[j].hit += 1

                        roomc.itemconfig(monsterlist[j].bat, image=self.fatBatDamage)
                        monsterlist[j].damagetimer = 0

                        if monsterlist[j].hit == monsterlist[j].health:
                            roomc.delete(monsterlist[j].bat)
                            monsterlist.pop(j)


                    except:
                        pass



        for i in range(len(monsterlist)-1):
            for k in range((len(monsterlist))-1,0,-1):
                if abs(roomc.coords(monsterlist[i].bat)[0]-roomc.coords(monsterlist[k].bat)[0])<70 and abs(roomc.coords(monsterlist[i].bat)[1]-roomc.coords(monsterlist[k].bat)[1])<60:
                    if roomc.coords(monsterlist[i].bat)[0]>roomc.coords(monsterlist[k].bat)[0]:
                        monsterlist[i].xspeed = 1
                        monsterlist[k].xspeed = -1
                    if roomc.coords(monsterlist[i].bat)[0]<roomc.coords(monsterlist[k].bat)[0]:
                        monsterlist[i].xspeed = -1
                        monsterlist[k].xspeed = 1
                    if roomc.coords(monsterlist[i].bat)[1] > roomc.coords(monsterlist[k].bat)[1]:
                        monsterlist[i].yspeed = 1
                        monsterlist[k].yspeed = -1
                    if roomc.coords(monsterlist[i].bat)[1] < roomc.coords(monsterlist[k].bat)[1]:
                        monsterlist[i].yspeed = -1
                        monsterlist[k].yspeed = 1
        for i in range(len(monsterlist)):
            self.x = roomc.coords(person)[0]
            self.y = roomc.coords(person)[1]
            if abs(roomc.coords(monsterlist[i].bat)[0]-self.x)<70 and abs(roomc.coords(monsterlist[i].bat)[1]-self.y)<60:
                if roomc.coords(monsterlist[i].bat)[0]>self.x:
                    monsterlist[i].xspeed = 2
                    roomc.move(person,-2,0)
                    if self.damagetimer>10:
                        self.damagetimer=0
                        self.health += -monsterlist[i].damage
                        roomc.coords(self.healthbar,100,self.tsize+25,self.health*3+100,self.tsize+55)
                if roomc.coords(monsterlist[i].bat)[0]<self.x:
                    monsterlist[i].xspeed = -2
                    roomc.move(person, 2, 0)
                    if self.damagetimer>20:
                        self.damagetimer=0
                        self.health += -monsterlist[i].damage
                        roomc.coords(self.healthbar, 100, self.tsize + 25, self.health * 3 + 100, self.tsize + 55)
                if roomc.coords(monsterlist[i].bat)[1] > self.y:
                    monsterlist[i].yspeed = 2
                    roomc.move(person, 0,-2)

                    if self.damagetimer>20:
                        self.damagetimer=0
                        self.health += -monsterlist[i].damage
                        roomc.coords(self.healthbar, 100, self.tsize + 25, self.health * 3 + 100, self.tsize + 55)

                if roomc.coords(monsterlist[i].bat)[1] < self.y:
                    monsterlist[i].yspeed = -2
                    roomc.move(person, 0,2)
                    if self.damagetimer>20:
                        self.damagetimer=0
                        self.health += -monsterlist[i].damage
                        roomc.coords(self.healthbar, 100, self.tsize + 25, self.health * 3 + 100, self.tsize + 55)

    def update(self):

        self.move()
        self.shoot()
        self.collision()
        self.x = roomc.coords(person)[0]-10
        self.y = roomc.coords(person)[1]-10
        self.timer+=1
        self.damagetimer+=1


        root1.after(17,self.update)



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
        root1.after(17,self.update)
    def move(self):
        roomc.move(self.tear,self.xspeed,self.yspeed)


class Enemy:
    def __init__(self,x,y):

        self.img = PhotoImage(file = "./FatBat.png")
        self.img=self.img.zoom(2,2)
        self.bat = roomc.create_image(x,y,image=self.img)

        self.health =50
        self.speed = 2.5
        self.speedgain = 0.05
        self.xspeed=self.speed
        self.yspeed = self.speed
        self.damagetimer = 0
        self.hit = 0
        self.damage = 15
        self.update()

    def update(self):
        self.damagetimer+=1
        self.chase()
        self.move()
        if self.damagetimer >4:
            roomc.itemconfig(self.bat, image=self.img)

        root1.after(17,self.update)

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



