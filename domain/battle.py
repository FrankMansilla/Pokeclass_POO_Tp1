#in process

from pokémon import Pokemon
from stats import Stats
from types import Type
from rival import Rival

def isNotDefeated(Stats): 
    return Stats.hp > 0

def defeated(Pokemon): 
    Pokemon.hp < 0
    return Pokemon.name, "Fainted!!"
    
def attack(self, Rival):
    beat = self.beat(Rival)
    Rival.hp = Rival.hp - beat
    print(self.name, "lost", beat, "of its health! ", Rival.name)
    if Rival.isNotDefeated():
        print("the hp of", Rival.name, "is", Rival.hp)
    else:
        Rival.defeated()