#Source: https://stackoverflow.com/questions/33586052/typeerror-unorderable-types-int-list
# Import Packages
import random

# Global Variables
perf_num = 500
species = [20]
temp_num = 0
length = 0
s = 0

# Main Program
for num in range(100):
    r1 = int(random.random()*10)
    r2 = int(random.random()*10)
    species.append(r1)
    length = len(species)
    while s < length:
        print(s)
        if species[s-1] > species[s]:
            temp_num = species[s-1] - r1
            species[s-1] = temp_num
        else:
            temp_num = species[s] - r1
            species[s] = temp_num
        if s-1 < 5:
            species[s-1] = []
        s += 1

    print(species)