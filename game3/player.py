from items import *
from map import rooms
player = {"inventory": [item_id, item_laptop, item_money],
          "equpied_weapon": item_laptop,
          "health": 100,
          "moves": 0,
          "current_room": rooms["Laboratory"]
          "mass": 0}

# Assign the players mass according to the mass of the items in their inventory
for item in player["inventory"]:
    player["mass"] += item["mass"]
