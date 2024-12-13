"""from time import perf_counter


iterator = range(10000000)
start_time = perf_counter()

result = []

for i in range(10000000):
    if i %2:
        result.append(i)

end_time = perf_counter()

print(end_time - start_time)

start_time = perf_counter()
comp_result = [i for i in iterator if not i %2]
end_time = perf_counter()

print(end_time - start_time)
"""

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
members = team_info['members']

name_superhero = [hero['name'] for hero in team_info['members']] 
print(name_superhero)

