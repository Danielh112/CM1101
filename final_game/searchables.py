from items import *
searchable_lobbydesk = {
    "id": "lobbydesk",
    "name": "the reception desk",
    "description": "A large rounded desk with many drawers, maybe there's something in there",
    "searchable": True,
    "items": [item_redflare]
}

searchable_labcoat = {
    "id": "labcoat",
    "name": "a labcoat",
    "description": "A long white labcoat, it looks like there is something in the front pocket.",
    "searchable": True,
    "items": [item_keys]
}

searchable_armorycabinet = {
    "id": "armorycabinet",
    "name": "a weapon cabinet",
    "description": "A tall grey racked cabinet.",
    "searchable": True,
    "items": [item_pistol]
}

searchable_medicalcabinet = {
    "id": "medicalcabinet",
    "name": "a medical cabinet",
    "description": "A small cupboard with a glass door",
    "searchable": True,
    "items": [item_medipac]
}

searchables = {
    "lobbydesk": searchable_lobbydesk,
    "labcoat": searchable_labcoat,
    "armorycabinet": searchable_armorycabinet,
    "medicalcabinet": searchable_medicalcabinet
}

# A function to actually search these items?
if input == "search" + ["searchables"]:
    if searchable == True:
        print(searchables["items"])
    else:
        print("You cannot search that")
else:
    pass