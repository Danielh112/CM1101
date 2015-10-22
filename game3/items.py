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
    "use": False
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

<<<<<<< HEAD

=======
>>>>>>> e89f351116d664c93479b044222e2e8a0d8991fe
def audioplayer_use():
    print("You turn on the audio player. That voice sounds very familiar.\n")
    wrap_print(""" 'All the work has paid off, I've finally cracked it. The secret to potential immortality.\nOur successful test subject *static* lies in front of me. I am the only one left in the lab, everyone\nelse has gone home to rest. We have a big day tomorrow. I'm about to perform some final checks to make sure\neveything is perfect for our presentation to the government officials tomorrow.'\n 'Turning on life support systems, the subject is responding'\n 'ERROR! ERROR! ERROR!'\n 'What?! What is wrong?!'\n 'No, no no! This cannot be happening, not now!'\n '(unintelligible growls and roars)'\nThe last thing on the recording is a sharp gasp, a huge smash and then...silence...   """)
    print("That sounds horrifying. Is that what happened here?\n.")

item_audioplayer = {
    "id": "audio player",
    "name": "an audio player",
    "description": """A run of the mill audio recorder.""",
    "damage": 0,
    "attainable": False,
    "use": audioplayer_use
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
    "green notebook": item_labnote4,
    "audio player": item_audioplayer
}
