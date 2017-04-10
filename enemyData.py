import tkinter as tk
def eNT(player,list,canvas):
    for i in range(len(list)):
        if abs(canvas.coords(list[i].pos)[0]-canvas.coords(player)[0]) <= 24 and abs(canvas.coords(list[i].pos)[1]-canvas.coords(player)[1]) <=24:
            return "nextTo"
        else:
            return "notnextTo"

class Enemy(object):
    def __init__(self,canvas,type):


        if type == "cave-spider":
            self.image = tk.PhotoImage(file = ".\PlayerPlaceHolder.png")
            self.pos = canvas.create_image(12,12,image = self.image)
            self.health = 10
            self.damage = 4
