import tkinter as tk
class Player():
    def __init__(self):
        self.health = 100
        self.strength = 0
        self.luck = 0
        self.charisma = 0
        self.gold = 0
        self.battleright = 0
        self.battleleft = 0
        self.battleup = 0
        self.battledown = 0

    def pstatadd(self,value):
        if value == "health":
            self.health += 10
        if value == "strength":
            if self.strength == 10:
                return False
            else:
                self.strength += 1
                return True
        if value == "luck":
            if self.luck == 10:
                return False
            else:
                self.luck += 1
                return True
        if value == "charisma":
            if self.charisma == 10:
                return False
            else:
                self.charisma += 1
                return True
    def gold(self,amount,function):
        if function.lower == "give":
            self.gold += amount
        elif function.lower == "take":
            self.gold -= amount
            if self.gold <= 0:
                self.gold = 0


player = Player()
class Items():
    def __init__(self, name, attack, armor, type):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.type = type
class Inventory():
    def __init__(self):
        self.items = {}
    def additem(self, item):
        self.items[item.name] = item
playerinventory = Inventory()
