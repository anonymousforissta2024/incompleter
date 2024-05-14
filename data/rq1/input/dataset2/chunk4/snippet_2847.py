#Source: https://stackoverflow.com/questions/51384612/python-typeerror-object-takes-no-parameters-while-class
from tank import Tank

tanks = {"a":Tank("Alice"), "b":Tank("Bob"), "c":Tank("Crane") }
alive_tanks = len(tanks)

while alive_tanks > 1:
    print()
    for tank_name in sorted(tanks):
        print(tank_name,tanks[tank_name])

    first = raw_input("Who fires ?").lower()
    second = raw_input("Who at ?").lower()

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError:
        print("No such Tank ")
        continue

    if not first_tank.alive or not second_tank.alive:
        print("One of those is dead!")
        continue

    print()
    print("*"*30)

    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1

    print("*"*30)

    for tank in tanks.value():
        if tank.alive:
            print(tank.name," is the winner !")
            break