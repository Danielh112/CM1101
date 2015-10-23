entity_zombie = {
    "id": "zombie",
    "name": "zombie",
    "alive": True,
    "hostile": True,
    "agression": 3,
    "health": 75,
    "damage": 25,
    "summary": "A zombie stands in the corner of the room.",
    "description": """You know you've seen this face before, a foggy memory of
swishing lab coats andtwitching limbs on an operating table flashes across your
conciousness. Its jaw is hanging off its face by a few tendons. Blood and flesh
drip from its jowls as it grunts unintelligibly. One arm seems to be bent in a
way that isn't humanly possible, the other holds a scalpel between its degloved
fingers. This must've been what decimated the lab."""
}

entity_old_man = {
    "id": "old man",
    "name": "old man",
    "alive": True,
    "hostile": False,
    "agression": 3,
    "name": "an old man",
    "health": 75,
    "damage": 25,
    "summary": "There is an old man stood in the corner.",
    "description": """At the end of the room, you see a shadowy hunched figure holding a cane. This old
    man must be a staff member from one of the other floors. He turns to face you, hearing you move about.
    You realize that this man isn't exactly 'complete'. One of his legs only goes as far as the knee,
    past which is just a mangled mess of muscle and bone. Grey tufts of hair still cling to the side of
    his head that is still present."""

}

entity_zombie_matt = {
    "id": "familiar zombie",
    "name": "zombie",
    "hostile": True,
    "agression": 3,
    "alive": True,
    "health": 75,
    "damage": 25,
    "summary": "A man in a ripped shirt wanders the room.",
    "description": """The first thing you notice is the ripped Pacman T-shirt,
fortunately what fabric is left covers what you assume is a hole straight
through the torso. It grunts at you,"intents...purposes...braiiiins".
You've heard that voice before, albeit not as guttural. You remember talking
with a friend about snakes, the sea and coffee. As odd as that seems,
you should probably focus on the violent situation at hand right now. """
}

entity_little_kid = {
    "id": "little kid",
    "name": "little kid",
    "hostile": True,
    "agression": 3,
    "alive": True,
    "health": 75,
    "damage": 25,
    "summary": "A little kid with a creepy mask stares at you.",
    "description": """"A little kid carrying a backpack and wearing what looks
like a a Halloween mask on her face is running about the room, knocking
everything over. She stops as soon as she realizes that you are there. She
lifts the mask, revealing a set of cold, dead eyes and a face that has been
ripped and torn. Her blonde ponytail falls to her shoulder, blood dripping
from the pink bow that fastens it. It would have been better for your sanity if
she kept the mask on. """
}

entity_zombie_electrician = {
    "id": "electrician",
    "name": "zombie",
    "hostile": True,
    "agression": 3,
    "alive": True,
    "health": 75,
    "damage": 25,
    "summary": "A zombie electrician is sat hunched over against the wall.",
    "description": """You see an electrician working with some wires in a hole
in the wall. A spark flies from the wires, illuminating the man's face. You see
that his lips have been forcibly removed, showing a full set of crooked,
bloodstained teeth. He raises his only remaining arm, grabbing one of the fizzling
wires and points it towards you, letting out an animalistic growl as he does so. """
}

entity_zombie_cleaner = {
    "id": "cleaner",
    "name": "zombie",
    "alive": True,
    "hostile": True,
    "agression": 3,
    "health": 75,
    "damage": 25,
    "summary": "A zombie stumbles around the room attempting to clean.",
    "description": """A woman shuffles towards you, dragging a red feather duster behind her. A line
of blood trails behind her, likely coming from the feather duster. You also notice that one of her eyes is
completely glazed over, the other so bloodshot that there seems to be no white left. She raises the feather
duster upon seeing you. What looks like human intestine falls out of the duster, splatting on the floor
with a horrible squelch."""
}

entities = {
    "zombie": entity_zombie,
    "old man": entity_old_man,
    "familiar zombie": entity_zombie_matt,
    "little kid": entity_little_kid,
    "electrician": entity_zombie_electrician,
    "cleaner": entity_zombie_cleaner
}
