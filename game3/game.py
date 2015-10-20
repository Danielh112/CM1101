from map import rooms
from player import *
from items import *
from gameparser import *
from entities import *
import string

move_commands = ["go", "flee", "leave", "move", "progress", "travel", "depart",
                 "escape", "exit", "journey", "withdraw"]

take_commands = ["take", "collect", "hold", "receive", "acquire", "attain",
                 "grasp", "clutch", "grasp", "grip", "obtain", "secure",
                 "snag", "snatch", "carry", "gain", "gather", "get"]

drop_commands = ["drop", "abandon", "dump", "release", "shed", "relinquish",
                 "unload"]

attack_commands = ["attack", "ambush", "assail", "assault", "charge", "harm",
                   "hurt", "rush"]


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_red_flare, item_dress])
    'red flare, dress'

    >>> list_of_items([item_shoes])
    'item_shoes'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_keys, item_batteries, item_pistol])
    'keys, batteries, pistol'
    """

    item_names = []
    for item in items:
        item_names.append(item["name"])

    item_name_string = ", ".join(item_names)
    return item_name_string


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room_items(rooms["Laboratory"])

    <BLANKLINE>
    >>> print_room_items(rooms["Lift Floor 1"])

    """
    room_items = room["items"]
    if not (len(room_items) == 0):
        print ("There is " + list_of_items(room_items) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    >>> print_inventory_items(inventory)
    You have id card, laptop, money with a combined weight of 3.7Kg.
    <BLANKLINE>
    """
    inventory = items
    if not (len(inventory) == 0):
        print ("You have " + list_of_items(inventory) +
               " with a combined weight of " + str(inventory_mass) + "Kg.\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    print("\n" + room["name"].upper() + "\n")
    print(room["description"] + "\n")
    print_room_items(room)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into
    which this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of
    commands related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like
    this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("Take " + item["id"].upper() + " to take " + item["name"])

    for item in inv_items:
        print("Drop " + item["id"].upper() + " to drop " + item["name"])

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid
    exit. It returns True if the exit is valid, and False otherwise. Assume
    that the name of the exit has been normalised by the function
    normalise_input(). For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
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
    else:
        print("You cannot go there")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    item = items[item_id]
    room_inventory = current_room["items"]
    if item in room_inventory:
        if (inventory_mass + item["mass"] <= 5.0):
            inventory.append(item)
            global inventory_mass
            inventory_mass += item["mass"]
            room_inventory.remove(item)
        else:
            print("You are carrying too much.")
    else:
        print("You cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there
    is no such item in the inventory, this function prints "You cannot drop
    that."
    """
    item = items[item_id]
    room_inventory = current_room["items"]
    if item in inventory:
        room_inventory.append(item)
        global inventory_mass
        inventory_mass -= item["mass"]
        inventory.remove(item)
    else:
        print("You cannot drop that.")


def execute_attack(entity_id, item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there
    is no such item in the inventory, this function prints "You cannot drop
    that."
    """
    # Player attacks entity
    entities[entity_id] -= items[item_id]["damage"]
    if entities[entity_id]["health"] <= 0:
        entities[entity_id]["alive"] = False

    # Entity attacks player
    health -= items[item_id]["damage"]
    if entities[entity_id]["health"] <= 0:
        entities[entity_id]["alive"] = False


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """
    if 0 == len(command):
        return

    if command[0] in move_commands:
        if len(command) > 1:
            execute_go(command[1])
            moves += 1
        else:
            print("Go where?")

    elif command[0] in take_commands:
        if len(command) > 1:
            execute_take(command[1])
            moves += 1
        else:
            print("Take what?")

    elif command[0] in drop_commands:
        if len(command) > 1:
            execute_drop(command[1])
            moves += 1
        else:
            print("Drop what?")

    elif command[0] in attack_commands:
        if len(command) > 2:
            if command[1] in current_room["entities"]:
                execute_attack(command[1], command[2])
            elif command[2] in current_room["entities"]:
                execute_attack(command[2], command[1])
            moves += 1
        else:
            print("Attack what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def check_victory():
    if len(rooms["Reception"]["items"]) == 6:
        print("You dropped all the items of at reception! You win.")
        return True
    else:
        return False


# This is the entry point of our program
def main():
    # Main game loop
    while True:
        # Check to see if player has won the game.
        if check_victory():
            break
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
