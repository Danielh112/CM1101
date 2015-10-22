from gameparser import wrap_text
from player import *

item_red_flare = {
    "id": "red flare",
    "name": "a red flare",
    "description": "You managed to find the red flare. Wow aren't you a special snowflake!",
    "damage": 0,
    "attainable": True,
    "use": False
}


def blue_flare_use():
    global blue_flare_used
    if current_room["name"] == "Roof":
        blue_flare_used = True
        print("The flare shoots of into the sky.")
    else:
        print("You cannot use the flare here.")

item_blue_flare = {
    "id": "blue flare",
    "name": "a blue flare",
    "description": "You even found the blue flare! Keep up the good work!",
    "damage": 0,
    "attainable": True,
    "use": False
}


def computer_use():
    print("You sit down at the computer.\n")
    print(wrap_text("""
You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west."""))
    print("\nLooks like a fun game but I should play this one first.")


def medipac_use():
    global health
    health = 100
    print("you are fully healed")


item_computer = {
    "id": "computer",
    "name": "a computer",
    "description": "It's running an old text-based adventure game, hah I remember when I made my first program.",
    "damage": 0,
    "attainable": False,
    "use": computer_use
}


item_pistol = {
    "id": "pistol",
    "name": "a pistol",
    "description": "You found a brand new kind of dirty pistol. Be careful! Don't kill too many people.",
    "damage": 100,
    "attainable": True,
    "use": False
}

item_dress = {
    "id": "dress",
    "name": "a little cocktail dress",
    "description": "Wow you found a little pink cocktail dress! It really brings out the colour in your eyes!",
    "damage": 0,
    "attainable": True,
    "use": False

}

item_shoes = {
    "id": "shoes",
    "name": "a pair of old shoes",
    "description": "This pair of shoes goes amazingly with the dress!",
    "damage": 0,
    "attainable": False,
    "use": False
}

item_keys = {
    "id": "keys",
    "name": "a set of keys",
    "description": "I wonder if they unlock anything.",
    "damage": 10,
    "attainable": True,
    "use": False
}

item_torch = {
    "id": "torch",
    "name": "a torch",
    "description": "Oh look this torch is brighter than my future.",
    "damage": 10,
    "attainable": True,
    "use": False
}

item_batteries = {
    "id": "batteries",
    "name": "some batteries",
    "description": "Why would you need batteries ?? Hmm, we'll see.",
    "damage": 0,
    "attainable": True,
    "use": False
}

item_water_gun = {
    "id": "water gun",
    "name": "a water gun",
    "description": "Not the most useful item in the current situation, maybe you could use it in the event of a very, very small fire?",
    "damage": 10,
    "attainable": True,
    "use": False
}

item_medipac = {
    "id": "medipac",
    "name": "a medipac",
    "description": "This medipac could come in handy in the event of a zombie attack! You should keep it safe.",
    "damage": 0,
    "attainable": True,
    "use": medipac_use
}

item_billy_idol_cd = {
    "id": "billy idol cd",
    "name": "a billy idol cd",
    "description": "Your favourite CD, a must have in the event of a zombie apocalypse",
    "damage": 5,
    "attainable": True,
    "use": False
}

item_saucepan = {
    "id": "saucepan",
    "name": "a saucepan",
    "description": "this could be used to cook food...or kill zombies, you choose.",
    "damage": 20,
    "attainable": True,
    "use": False
}

items = {
    "computer": item_computer,
    "red flare": item_red_flare,
    "blue flare": item_blue_flare,
    "pistol": item_pistol,
    "dress": item_dress,
    "shoes": item_shoes,
    "keys": item_keys,
    "torch": item_torch,
    "batteries": item_batteries,
    "medipac": item_medipac,
    "billy idol cd": item_billy_idol_cd,
    "water gun": item_water_gun,
    "saucepan": item_saucepan
}
