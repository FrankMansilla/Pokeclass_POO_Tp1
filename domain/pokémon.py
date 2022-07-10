from stats import Stats
from types import Type
from moves import Moves
import logging

#configuration
logging.basicConfig(filename='logs.POKECLASS_POO_TP1', level=logging.INFO)

#     #test variables
#     host = 'www.pokeclass.co'
#     product_id = 'id-3359'
#     archive = 'none'
#     working_mode = 'r'

#     #diagnostic logs
#     logging.info('information of')





class Pokemon(Stats, Type, Moves):

    name = str
    elementalType1 = Type
    Move1 = Moves
    HP = Stats
    attack = Stats
    defence = Stats
    velocity = Stats
#caught = bool
#nature = str
#condition = str
#elementalType2 = str

    """""setters"""
    def __init__(self, name, Type, Moves, HP, attack, defence, velocity):
        self.name = name
        self.elementalType1 = Type
        self.Move1 = Moves
        self.Stats = HP
        self.Stats = attack
        self.Stats = defence
        self.Stats = velocity
#self.elementalType2 = elementalType2
#self.caugth = caught
#self.nature = nature
#self.condition = condition

    def atributes(self):
        logging.info("Name: %s", self.name)
        logging.info("Type: %s", self.elementalType1)
        logging.info("Move One: %s", self.Move1)
        logging.info("Stats: ")
        input("HP: ")
        input("attack: ")
        input("defence: ")
        input("velocity: ")
#print("Type Two:", self.elementalType2)
#print("caught:", self.caugth)
#print("nature:", self.nature)
#print("condition:", self.condition)
