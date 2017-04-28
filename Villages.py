import random
import tkinter as tk

class Villager():
    def __init__(self):
        self.items = {}
        self.villagertype = 0
    def additem(self, item):
        self.items[item.name] = item

class Village():
    def __init__(self):
        self.population = random.randint(3,10)
        self.friend = 50
        villagers = [0]
        for i in range (1,self.population+1):
            villagers.append(self, random.randint(1,5))
        for i in range (1,len(list)):

        villager1 = tk.PhotoImage(file = "")
        villager2 = tk.PhotoImage(file = "")
        villager3 = tk.PhotoImage(file = "")
        villager4 = tk.PhotoImage(file = "")
        villager5 = tk.PhotoImage(file = "")
    def addfriend (self, value):
        self.friend += value
village1 = Village