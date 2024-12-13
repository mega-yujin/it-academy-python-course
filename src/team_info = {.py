team_info = {
    "squad_name": "Super hero squad",
    "home_town": "Metro City",
    "formed": 2024,
    "secret_base": "Super tower",
    "active": True,
    "members": [
        {
            "name": "Molecule Man",
            "age": 29,
            "secret_identity": "Dan Jukes",
            "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast",
                "Teleportation",
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secret_identity": "Jane Wilson",
            "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Radiation resistance",
                "Radiation blast",
                "Heat Immunity",
                "Superhuman reflexes",
            ]
        },
        {
            "name": "Eternal Flame",
            "age": 1000000,
            "secret_identity": "Unknown",
            "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
            ]
        },
    ]
}

#unique_abilities = {power for member in team_info['members'] for power in member['powers']}
#print(unique_abilities)

"""for member in team_info['members']:
    for power in members['powers']:
        unique_abilities.add(power)
        print(unique_abilities)
"""

hero = {info['name'] :info['powers'] for info in team_info['members']}

print(hero)


