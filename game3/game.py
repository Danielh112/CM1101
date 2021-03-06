from map import rooms
from player import *
from items import *
from gameparser import *
from entities import *
from descriptions import *
import string


verbs = {
    "move": ["go", "move", "travel", "run", "walk", "jog", "flee",
             "progress", "escape", "journey"],

    "take": ["take", "collect", "acquire", "attain", "obtain", "carry",
             "grasp", "clutch", "grip", "snatch", "gain", "grab", "steal"
             "pick", "pickup"],

    "drop": ["drop", "dump", "abandon", "release", "relinquish"],

    "attack": ["attack", "kill", "ambush", "assail", "charge", "harm", "hurt"],

    "look": ["look", "stare", "view", "notice", "glance", "admire", "study",
             "gaze", "inspect", "scout", "scan", "survey", "examine", "read"],

    "use": ["use", "operate", "work"]
}

nouns = {
    "inventory": ["inv", "invent", "inventory"],

    "self": ["self", "myself", "injuries", "injury"]
}


def print_condition():
    if health <= 20:
        wrap_print("You're pretty much dead mate.")
    elif health <= 40:
        wrap_print("You have a horrible gash on your lower left leg. If left it'll probably turn septic.")
    elif health <= 60:
        wrap_print("You have a few scrapes and cuts but for the most part you're okay.")
    elif health <= 80:
        wrap_print("Your clothes are a bit torn and you look a bit grubby, what would your mum say!.")
    elif health <= 100:
        wrap_print("You're fine stop complaining.")


def list_of_objects(objects):
    """This function takes a dictionary of objects and returns a ascendingly sorted
    comma-separated sentence of object names (as a string).

    >>> list_of_objects({"red flare": item_red_flare, "dress": item_dress})
    'a little cocktail dress and a red flare'

    >>> list_of_objects({"shoes": item_shoes})
    'a pair of old shoes'

    >>> list_of_objects({"keys": item_keys, "batteries": item_batteries, "pistol": item_pistol})
    'a pistol, a set of keys and some batteries'

    >>> list_of_objects({})
    ''
    """
    # Create a list of item_names.
    object_name = [obj["name"] for obj in objects.values()]
    object_name = sorted(object_name)
    # Create an indexable dictionary for the final sentence.
    sentence = {}
    for x in range(0, len(object_name)):
        # Assign every other word in dictionary an item name.
        sentence[x * 2] = object_name[x]
        # Fill in empty entries with joining strings.
        if x != len(object_name) - 1:
            sentence[x * 2 + 1] = ", "
        elif len(object_name) > 1:
            sentence[x * 2 - 1] = " and "
    return "".join(sentence.values())


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed.

    >>> print_room_items(rooms["Laboratory"])
    There is a billy idol cd, a computer and a saucepan here.

    >>> print_room_items(rooms["Changing Area"])
    There is a little cocktail dress and a pair of old shoes here.

    >>> print_room_items(rooms["Roof"])
    There is nothing here.
    """
    room_items = room["items"]
    if (len(room_items) != 0):
        return " There is " + list_of_objects(room_items) + " here."
    else:
        return " There are no items here."


def print_room_entities(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed.

    >>> print_room_items(rooms["Laboratory"])
    There is a billy idol cd, a computer and a saucepan here.

    >>> print_room_items(rooms["Changing Area"])
    There is a little cocktail dress and a pair of old shoes here.

    >>> print_room_items(rooms["Roof"])
    There is nothing here.
    """
    room_entities = room["entities"]
    if (len(room_entities) != 0):
        entity_descriptions = ""
        for entity in room_entities.values():
            if entity["alive"]:
                entity_descriptions += entity["summary"]
            else:
                entity_descriptions += "A " + entity["name"] + " corpse lies on the ground."
        return " " + entity_descriptions
    else:
        return " You are by yourself in here."


def entity_get_id_from_name(entiy_name, entity_list):
    for entity in entity_list:
        if entity["name"] == entiy_name:
            return entity["id"]
    return False


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here." and if you do not have
    any items in your inventory this funciton prints "You don't have anything.".

    >>> print_inventory_items({"billy idol cd": item_billy_idol_cd, "saucepan": item_saucepan})
    You have a billy idol cd and a saucepan.
    <BLANKLINE>

    >>> print_inventory_items({"red flare": item_red_flare})
    You have a red flare.
    <BLANKLINE>
    """
    if not (len(items) == 0):
        wrap_print("You have " + list_of_objects(items) + ".\n")
    else:
        wrap_print("You don't have anything.\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Laboratory"])
    <BLANKLINE>
    LABORATORY
    <BLANKLINE>
    You see flames flicker in the corner of the room. There are holes in the
    wall, showing exposed wiring. Most of your equipment has been destroyed. The
    security door to the west of the room has been wrenched open, whereas the doors
    to the east (Infirmary) and north (Changing Area) remain untouched.
    There is a billy idol cd, a computer and a saucepan here.

    >>> print_room(rooms["Changing Area"])
    <BLANKLINE>
    CHANGING AREA
    <BLANKLINE>
    This must be where the scientists change into their lab gear.
    Lockers line the west wall, numbered from 1-20. The door to the south leads
    to the lab.
    There is a little cocktail dress and a pair of old shoes here.

    >>> print_room(rooms["Canteen"])
    <BLANKLINE>
    CANTEEN
    <BLANKLINE>
    The door to the canteen is locked, probably because you seem to be the
    only one here. Your stomach rumbles, almost in response to the locked door.
    There is a water gun here.
    """
    cls()
    print("\n" + room["name"].upper() + "\n")
    wrap_print(room["description"] + print_room_items(room) + print_room_entities(room))


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into
    which this exit leads. For example:

    >>> exit_leads_to(rooms["Laboratory"]["exits"], "east")
    'Infirmary'
    >>> exit_leads_to(rooms["Changing Area"]["exits"], "south")
    'Laboratory'
    >>> exit_leads_to(rooms["Armory"]["exits"], "east")
    'Changing Area'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    wrap_print("GO " + direction.upper() + " to " + leads_to + ".")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid
    exit. It returns True if the exit is valid, and False otherwise. Assume
    that the name of the exit has been normalised by the function
    normalise_input(). For example:

    >>> is_valid_exit(rooms["Laboratory"]["exits"], "east")
    True
    >>> is_valid_exit(rooms["Laboratory"]["exits"], "south")
    False
    >>> is_valid_exit(rooms["Changing Area"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Changing Area"]["exits"], "south")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        current_room = move(current_room["exits"], direction)
        print_room(current_room)
        global valid_move
        valid_move = True
    else:
        wrap_print("You cannot go there")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    dictionary of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    if (item_id in current_room["items"]) and (items[item_id]["attainable"]):
        inventory[item_id] = current_room["items"][item_id]
        del current_room["items"][item_id]
        wrap_print(inventory[item_id]["description"])
        global valid_move
        valid_move = True
    else:
        wrap_print("You cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to dictionary of items in the current room. However, if there
    is no such item in the inventory, this function prints "You cannot drop
    that."
    """
    if (item_id in inventory):
        current_room["items"][item_id] = inventory[item_id]
        del inventory[item_id]
        wrap_print("You dropped " + items[item_id]["name"] + ".")
        global valid_move
        valid_move = True
    else:
        wrap_print("You cannot drop that.")


def execute_use(item_id):
    """This function takes an item_id as an argument and executes the function
    associated with the use of the item. If the item has no use, this function
    prints "You cannot use that." If the item is not in the players inventory or
    in the room, this fucntion prints "You can't see that in the room."
    """
    if (item_id in inventory.keys()) or (item_id in current_room["items"].keys()):
        if items[item_id]["use"] != False:
            items[item_id]["use"]()
            global valid_move
            valid_move = True
        else:
            wrap_print("You cannot use that.")
    else:
        wrap_print("You can't see that in the room.")


def attack_entity(entity_id, item_id):
    global health
    entities[entity_id]["health"] -= items[item_id]["damage"]
    entities[entity_id]["hostile"] = True
    entities[entity_id]["agression"] = 0
    if entities[entity_id]["health"] <= 0:
        entities[entity_id]["alive"] = False
        wrap_print("You attack the " + entities[entity_id]["name"] + " with a " + item_id + " and kill it.")
    else:
        wrap_print("You attack the " + entities[entity_id]["name"] + " with a " + item_id + ".")


def entity_attacks(entity_id):
    global health
    global alive
    if entities[entity_id]["alive"] == True:
        health -= entities[entity_id]["damage"]
        if health <= 0:
            alive = False
        wrap_print("The " + entities[entity_id]["name"] + " injures you.")


def check_entity_attacks():
    for entity in current_room["entities"].values():
        if entity["hostile"] == True:
            if entity["agression"] == 0:
                entity_attacks(entity["id"])
            else:
                entity["agression"] -= 1
                if entity["agression"] == 0:
                    print("The " + entity["name"] + " becomes enraged.")
                    entity_attacks(entity["id"])
                else:
                    print("The " + entity["name"] + " is getting agitated.")


def execute_attack(entity_id, item_id):
    if entities[entity_id]["alive"] == False:
        wrap_print("A " + entity_id + " corpse lies on the ground.")
    else:
        attack_entity(entity_id, item_id)
        global valid_move
        valid_move = True


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input). The leading word is checked against a list of verbs,
    and depending on the verb match a command is executed.
    """
    if 0 == len(command):
        return

    if command[0] in verbs["move"]:
        if len(command) <= 1:
            wrap_print("go where?")
        else:
            execute_go(command[1])

    elif command[0] in verbs["take"]:
        if len(command) <= 1:
            wrap_print("Take what?")
        else:
            item_id = get_multi_word_string(command, items)
            execute_take(item_id)

    elif command[0] in verbs["drop"]:
        if len(command) <= 1:
            wrap_print("Drop what?")
        else:
            item_id = get_multi_word_string(command, items)
            execute_drop(item_id)

    elif command[0] in verbs["use"]:
        if len(command) <= 1:
            wrap_print("use what?")
        else:
            item_id = get_multi_word_string(command, current_room["items"])
            if item_id is False:
                item_id = get_multi_word_string(command, inventory)
            execute_use(item_id)

    elif command[0] in verbs["look"]:
        if len(command) == 1:
            print_room(current_room)
        elif command[1] in nouns["inventory"]:
                print_inventory_items(inventory)
        elif command[1] in nouns["self"]:
                print_condition()
        else:
            item_id = get_multi_word_string(command, current_room["items"])
            if item_id is False:
                item_id = get_multi_word_string(command, inventory)
            entity_name = get_multi_word_string(command, [entity["name"] for entity in current_room["entities"].values()])
            entity_id = entity_get_id_from_name(entity_name, current_room["entities"].values())
            if item_id in inventory.keys():
                wrap_print(items[item_id]["description"])
            elif item_id in current_room["items"].keys():
                wrap_print(items[item_id]["description"])
            elif entity_id in current_room["entities"].keys():
                wrap_print(entities[entity_id]["description"])
            else:
                wrap_print("You can not view that.")

    elif command[0] in verbs["attack"]:
        if len(command) > 2:
            item_id = get_multi_word_string(command, items)
            entity_name = get_multi_word_string(command, [entity["name"] for entity in current_room["entities"].values()])
            entity_id = entity_get_id_from_name(entity_name, current_room["entities"].values())
        if len(command) <= 1:
            wrap_print("attack what?")
        elif entity_id not in current_room["entities"].keys():
            wrap_print("You cannot attack that.")
        elif len(command) <= 2:
            wrap_print("What with?")
        elif item_id not in inventory.keys():
            wrap_print("You do not have a that item.")
        elif items[item_id]["damage"] == False:
            wrap_print("You cannot attack using that item.")
        else:
            execute_attack(entity_id, item_id)

    elif command[0] == "help":
        print("To move in a given direction type:     go     <DIRECTION>")
        print("To pick up an item type:               take   <ITEM>")
        print("To drop an item type:                  drop   <ITEM>")
        print("To use an item type:                   use    <ITEM>")
        print("To look at something of interest type: view   <ITEM>")
        print("to attack a character type:            attack <CHARACTER> with <item>")
        print("to :            attack <CHARACTER> with <item>")
        print("To quit the game type:                 quit\n")
        wrap_print("""Verb variations are supported, so 'run south', or 'inspect item' are valid inputs.""")
        wrap_print("""Items and characters with multiple words in their name are also supported like regular items.""")

    elif command[0] == "quit":
        if len(command) == 1:
            wrap_print("goodbye!")
            global playing
            playing = False

    else:
        wrap_print("That makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of available exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Laboratory"]["exits"], "north") == rooms["Changing Area"]
    True
    >>> move(rooms["Changing Area"]["exits"], "south") == rooms["Laboratory"]
    True
    >>> move(rooms["Armory"]["exits"], "east") == rooms["Laboratory"]
    False
    """
    return rooms[exits[direction]]

def music():
    import winsound
    winsound.PlaySound("This_House.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
<<<<<<< HEAD
=======

>>>>>>> e89f351116d664c93479b044222e2e8a0d8991fe


def check_victory():
    global current_room
    if current_room["name"] == "Roof":
        return True


def advance_move():
    global valid_move
    if valid_move:
        if check_victory():
            return True
        check_entity_attacks()
        if not alive:
            wrap_print("You died!")
            return True
        global moves
        moves += 1
        valid_move = False


# This is the entry point of our program
def main():
    # music()
    # Main game loop
    print_room(current_room)
    while playing:
        # Show the menu with possible actions and ask the player
        print("")
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        if advance_move():
            break


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
