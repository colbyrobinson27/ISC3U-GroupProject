import random
class Economy:
    def __init__(self,biome,race):
        self.biome = biome
        self.race = race
        self.economy = self.goodsProd()
    def goodsProd(self):
        if self.biome == 'mountains':
            if self.race == 'dwarf':
                return (random.choice(['mining','weapons','metal refining']))
            elif self.race == 'goblin'

def priceCalc(default,supply,demand):
    return((default/(supply/10))*demand)
