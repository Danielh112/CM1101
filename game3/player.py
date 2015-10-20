from items import *
from map import rooms

inventory = []
moves = 0
# Start game at the reception
current_room = rooms["Laboratory"]
# Work out the inital weight of item in the players invientory.
inventory_mass = 0
for item in inventory:
    inventory_mass += item["mass"]
