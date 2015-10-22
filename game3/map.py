from items import *
from entities import *

room_lab = {
    "name": "Laboratory",

    "description":
    """You see flames flicker in the corner of the room. There are holes in the
wall, showing exposed wiring. Most of your equipment has been destroyed. The
security door to the west of the room has been wrenched open, whereas the doors
to the east (Infirmary) and north (Changing Area) remain untouched.""",

    "exits": {"east": "Infirmary", "north": "Changing Area",
              "west": "Lift Floor 2"},

    "items": {"billy idol cd": item_billy_idol_cd, "clip board": item_clip_board,
              "computer": item_computer, "notebook": item_labnote1},

    "entities": {"generic zombie": entity_zombie}
}

room_changingarea = {
    "name": "Changing Area",

    "description":
    """This must be where the scientists change into their lab gear.
Lockers line the west wall, numbered from 1-20. The door to the south leads
to the lab. You notice that locker 16 has come away from the wall leaving a doorway in the west wall.""",

    "exits": {"south": "Laboratory", "west": "Armory"},

    "items": {"dress": item_dress, "shoes": item_shoes, "red notebook": item_labnote2},

    "entities": {}
}

room_armory = {
    "name": "Armory",

    "description":
    """There's a secret armoury behind locker 16, who knew?
This must be for emergencies. All but one the cabinets that line all 4 walls
are locked and require a keycode to open. To the east is the hole in the wall that leads back to the changing area""",

    "exits": {"east": "Changing Area"},

    "items": {"pistol": item_pistol, "torch": item_torch},

    "entities": {}
}

room_basement = {
    "name": "Storage Basement",

    "description":
    """Large glass tubes line the northern end of the room. This looks like a
storage area for test subjects. The glass tube in the middle has been
smashed. The tube is labelled, "Prototype - M. Morgan, 'To all intents
and purpsoes, a failed test subject'". The southern end of the room is
lined with cupboards and cabinets. In between the cabinets is the door to
the lift.""",

    "exits": {"south": "Lift Floor 1"},

    "items": {"blue flare": item_blue_flare},

    "entities": {"old man": entity_old_man}
}

room_infirmary = {
    "name": "Infirmary",

    "description":
    """This room is the only clean room in the complex. It feels too clinical.
Cabinets filled with various medical supplies line the north and east walls.
The west door leads back to the lab.""",

    "exits": {"west": "Laboratory"},


    "items": {"health pack": item_health_pack, "blue notebook": item_labnote3},

    "entities": {}
}

room_lobby = {
    "name": "Lobby",

    "description":
    """The door to the outside is blocked by large pieces of rubble.
The reception lies in ruin. One of the drawers is still intact and is
lying open. The door to the east leads to the lift area.""",

    "exits": {"east": "Lift Floor 3"},

    "items": {"red flare": item_red_flare, "green notebook": item_labnote4},

    "entities": {"little boy": entity_little_kid}
}

room_canteen = {
    "name": "Canteen",

    "description":
    """The door to the canteen is locked, probably because you seem to be the
only one here. Your stomach rumbles, almost in response to the locked door. There is a stairwell to
the north and the lift to the east.
""",

    "exits": {"east": "Lift Floor 4", "north": "Stairs"},

    "items": {"water gun": item_water_gun},

    "entities": {}
}

room_roof = {
    "name": "Roof",

    "description":
    """The helipad takes up most of the roofspace. Big time executives and
government officials must use this for lab visits. You see a helicopter
flying over one of the buildings on the other side of the city. The stairwell is on the east side of the
building.
""",

    "exits": {"east": "Stairs"},

    "items": {},

    "entities": {"Dr. Matt the zombie": entity_zombie_matt}
}

room_stairs = {
    "name": "Stairs",

    "description":
    """This stairwell is looking a bit worse for wear because no one actually
uses the stairs. Scientists don't tend to be the fittest people. Another stairwell runs west that will take you to the roof.
The southern stairs lead back to the canteen.""",

    "exits": {"west": "Roof", "south": "Canteen"},

    "items": {"batteries": item_batteries},

    "entities": {"zombie cleaner": entity_zombie_cleaner}
}

room_lift1 = {
    "name": "Lift Floor 1",

    "description":
    """The lift is pretty unremarkable, it's a lift, what do you expect?.
There's a keypad beside the door with 4 buttons numbered 1-4. Do you want to go up a floor? You can also go west from this location.""",

    "exits": {"up": "Lift Floor 2", "west": "Storage Basement"},

    "items": {},

    "entities": {}
}

room_lift2 = {
    "name": "Lift Floor 2",

    "description":
    """The lift is pretty unremarkable, it's a lift, what do you expect?.
There's a keypad beside the door with 4 buttons numbered 1-4. Do you want to go up or down a floor? You can also go east from this location.  """,

    "exits": {"down": "Lift Floor 1", "up": "Lift Floor 3", "east": "Laboratory"},

    "items": {},

    "entities": {}
}

room_lift3 = {
    "name": "Lift Floor 3",

    "description":
    """The lift is pretty unremarkable, it's a lift, what do you expect?.
There's a keypad beside the door with 4 buttons numbered 1-4. Do you want to go up or down a floor? You can also go west from this location. """,

    "exits": {"down": "Lift Floor 2", "up": "Lift Floor 4", "west": "Lobby"},

    "items": {},

    "entities": {"zombie electrician": entity_zombie_electrician}
}

room_lift4 = {
    "name": "Lift Floor 4",

    "description":
    """The lift is pretty unremarkable, it's a lift, what do you expect?.
There's a keypad beside the door with 4 buttons numbered 1-4. Do you want to go up or down a floor? You guessed it! You can go west too. """,

    "exits": {"down": "Lift Floor 3", "west": "Canteen"},

    "items": {},

    "entities": {}
}

rooms = {
    "Laboratory": room_lab,
    "Changing Area": room_changingarea,
    "Armory": room_armory,
    "Storage Basement": room_basement,
    "Infirmary": room_infirmary,
    "Lobby": room_lobby,
    "Canteen": room_canteen,
    "Roof": room_roof,
    "Lift Floor 1": room_lift1,
    "Lift Floor 2": room_lift2,
    "Lift Floor 3": room_lift3,
    "Lift Floor 4": room_lift4,
    "Stairs": room_stairs
}


from gameparser import wrap_print
inventory = {}
blue_flare_used = False
item_red_flare = {
    "id": "red flare",
    "name": "a red flare",
    "description": "You managed to find the red flare. Wow aren't you a special snowflake!",
    "damage": False,
    "attainable": True,
    "use": False
}


def blue_flare_use():
    global current_room
    if current_room["name"] == "Roof":
        blue_flare_used = True
        print("The flare shoots of into the sky.")
    else:
        print("You cannot use the flare here.")

item_blue_flare = {
    "id": "blue flare",
    "name": "a blue flare",
    "description": "You even found the blue flare! Keep up the good work!",
    "damage": False,
    "attainable": True,
    "use": blue_flare_use
}


def computer_use():
    print("You sit down at the computer.\n")
    wrap_print("""
You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""")
    print("\nLooks like a fun game but I should play this one first.")


item_computer = {
    "id": "computer",
    "name": "a computer",
    "description": "It's running an old text-based adventure game, hah I remember when I made my first program.",
    "damage": False,
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
    "damage": False,
    "attainable": True,
    "use": False

}

item_shoes = {
    "id": "shoes",
    "name": "a pair of old shoes",
    "description": "This pair of shoes goes amazingly with the dress!",
    "damage": False,
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
    "damage": False,
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


def heatlh_pack_use():
    global health
    health = 100
    print("you are fully healed")
    global inventory
    del inventory["health pack"]


item_health_pack = {
    "id": "health pack",
    "name": "a health pack",
    "description": "This health pack could come in handy in the event of a zombie attack! You should keep it safe.",
    "damage": False,
    "attainable": True,
    "use": heatlh_pack_use
}

item_billy_idol_cd = {
    "id": "billy idol cd",
    "name": "a billy idol cd",
    "description": "Your favourite CD, a must have in the event of a zombie apocalypse",
    "damage": 5,
    "attainable": True,
    "use": False
}

item_clip_board = {
    "id": "clip board",
    "name": "a clip board",
    "description": "Made of metal. Good for taking notes ...or killing zombies, you choose.",
    "damage": 30,
    "attainable": True,
    "use": False
}

item_labnote1 = {
    "id": "notebook",
    "name": "a notebook",
    "description": """DAY 23\nI'm getting closer, my team and I have been striving towards the secret to extending\nhuman life and there's been a promising chemical cocktail required to keep a person's systems working\nefficiently. It's been dubbed "The Elixir of Life" by my colleagues, I prefer to simply call it\nvorodisone. It's showing great results, beyond our projections, when used on the lab rats. I hope\nwe get approval for a human subject soon, our research can only go so far using animal test\nsubjects. """,
    "damage": 0,
    "attainable": False,
    "use": False
}

item_labnote2 = {
    "id": "red notebook",
    "name": "a red notebook",
    "description": """DAY 40\nAppoval for human test subjects has finally come through. Fantastic, research has been in\nstasis since the vorodisone breakthrough earlier in the month. Our first test subject is actually an old\nfriend of mine, Matt from university. He volunteered himself, hoping to further my research. Preliminary\nresults don't seem to be as amazing as once hoped, maybe the doses need some fine tuning.""",
    "damage": 0,
    "attainable": False,
    "use": False
}

item_labnote3 = {
    "id": "blue notebook",
    "name": "a blue notebook",
    "description": """DAY 55\nMy motivation to continue has been completely quashed. Matt accidentally self-administered\n2 doses last week. The large influx of chemicals took a huge toll on his body. He was in intensive care with\nmultiple organ failure, finally succumbing to the pain and suffering yesterday. Before he passed away, he\nmade me promise to continue with my work and actually donated his body to our lab, in effect after his death.\nIt's too distressing for me, seeing an old friend's body being stored in our basement, so I haven't been\ndoing much work, but my colleagues say that they're learning where we went wrong. """,
    "damage": 0,
    "attainable": False,
    "use": False
}

item_labnote4 = {
    "id": "green notebook",
    "name": "a green notebook",
    "description": """DAY 70\nA new test subject arrived two days ago. They wish to remain anonymous. My motivation\nto finish this has finally returned, I understand it's what Matt would've wanted. My team have ensured\nthat this new balance and dosage of vorodisone will work. Our results are proving to be extremely\npromising, I have actually informed my team that we are ready to present it to the world next week.\nThis could be it, my life's work complete. But at what cost? What effect will this have on the world?""",
    "damage": 0,
    "attainable": False,
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
    "health pack": item_health_pack,
    "billy idol cd": item_billy_idol_cd,
    "water gun": item_water_gun,
    "clip board": item_clip_board,
    "notebook": item_labnote1,
    "red notebook": item_labnote2,
    "blue notebook": item_labnote3,
    "green notebook": item_labnote4
}
