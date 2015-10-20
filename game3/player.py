from items import *
from map import rooms
player = {
"inventory":[item_id, item_laptop, item_money],
"equpied_weapon": item_laptop,
"health" :100,
"moves" :0,
# Start game at the reception
"current_room": rooms["Reception"]
# Work out the inital weight of item in the players invientory.
"inventory_mass": 0}
for item in inventory:
    inventory_mass += item["mass"]
