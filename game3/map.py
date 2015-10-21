from items import *
from entities import *

room_lab = {
    "name": "Laboratory",

    "description":
    """You see flames flicker in the corner of the room. There are holes in the
wall, showing exposed wiring. Most of your equipment has been destroyed. The
security door to the west of the room has been wrenched open, whereas the doors
to the east (Infirmary) and north (Changing Area) remain untouched.
""",

    "exits": {"east": "Infirmary", "north": "Changing Area",
              "west": "Lift Floor 2"},

    "items": {"billy idol cd": item_billy_idol_cd, "saucepan": item_saucepan,
              "computer": item_computer},

    "entities": {"zombie": entity_zombie }
}

room_changingarea = {
    "name": "Changing Area",

    "description":
    """This must be where the scientists change into their lab gear.
Lockers line the west wall, numbered from 1-20. The door to the south leads
to the lab.""",

    "exits":  {"south": "Laboratory"},

    "items": {"dress": item_dress, "shoes": item_shoes},

    "entities": {}
}

room_armory = {
    "name": "Armory",

    "description":
    """There’s a secret armory behind locker 16. Who knew?.
This must be for emergencies. All but one the cabinets that line all 4 walls
are locked and require a keycode to open.""",

    "exits": {"east": "Changing Area"},

    "items": {"pistol": item_pistol, "torch": item_torch},

    "entities": {}
}

room_basement = {
    "name": "Storage Basement",

    "description":
    """Large glass tubes line the northern end of the room. This looks like a
storage area for test subjects. The glass tube in the middle has been
smashed. The tube is labelled, “Prototype - M. Morgan, ‘To all intents
and purposes, a failed test subject’”. The southern end of the room is
lined with cupboards and cabinets. In between the cabinets is the door to
the stairwell.""",

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

    "items": {"medipac": item_medipac},

    "entities": {}
}

room_lobby = {
    "name": "Lobby",

    "description":
    """The door to the outside is blocked by large pieces of rubble.
The reception lies in ruin. One of the drawers is still intact and is
lying open. The door to the east leads to the lift area.
""",

    "exits": {"east": "Lift Floor 3"},

    "items": {"red flare": item_red_flare},

    "entities": {"little kid": entity_little_kid}
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
uses the stairs. Scientists don't tend to be the fittest people. """,

    "exits": {"west": "Roof"},

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
There's a keypad beside the door with 4 buttons numbered 1-4. Do you want to go up or down a floor? You can also go west from this location.  """,

    "exits": {"down": "Lift Floor 1", "up": "Lift Floor 3", "west": "Laboratory"},

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
    "Basement": room_basement,
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
