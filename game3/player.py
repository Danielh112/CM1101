from items import *
from map import rooms

current_room = rooms["Laboratory"]
inventory = []
equpied_weapon = item_water_gun
health = 100
moves = 0
mass = 0

# Assign the players mass according to the mass of the items in their inventory
for item in inventory:
    mass += item["mass"]
