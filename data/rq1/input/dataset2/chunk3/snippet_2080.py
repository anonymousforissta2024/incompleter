#Source: https://stackoverflow.com/questions/61043476/how-do-i-fix-a-typeerror-in-python
from Classes.game import player, bcolors

magic = [{"name": "Tackle", "cost": 1, "dmg": 4},
         {"name": "Ember", "cost": 3, "dmg": 6},
         {"name": "Leech", "cost": 4, "hp": +5, "dmg": 4},
         {"name": "Explosion", "cost": 5, "hp": -10, "dmg": 30}]

player(100, 20, 5, 10,magic)

print(player.generate_damage())