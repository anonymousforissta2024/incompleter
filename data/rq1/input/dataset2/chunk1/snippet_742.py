#Source: https://stackoverflow.com/questions/43477958/typeerror-not-supported-between-instances-python
import random


class part():
    def __init__(self, number):
        self.number = number
        self.machine_sequence = []

    def add_volume(self, volume):
        self.volume = volume

    def add_machine(self, machine_numbers):
        self.machine_sequence.append(machine_numbers)


def create_initial_population():
    part_family = []

    for i in range(8):
        part_family.append(part(i))

    part_population = []

    for i in range(6):
        part_population.append(random.sample(part_family, len(part_family)))

    for i in part_population:
        for j in i:
            j.add_volume(random.randrange(100, 200))

    return part_population


def fitness(part_family):
    sum_of_boundary = []
    for i in range(0, 8, 2):
        sum_of_boundary.append(sum(j.volume for j in part_family[i:i + 2]))

    fitness_value = 0

    for i in range(len(sum_of_boundary) - 1):
        for j in range(i + 1, len(sum_of_boundary)):
            fitness_value = fitness_value + abs(sum_of_boundary[i] - sum_of_boundary[j])

    return fitness_value


def sort_population_by_fitness(population):
    pre_sorted = [[fitness(x),x] for x in population]
    sort = [x[1] for x in sorted(pre_sorted)]
    for i in sort:
        for j in i:
            print(j.volume, end = ' ')
        print()

    return sort


def evolve(population):
    population = sort_population_by_fitness(population)
    return population


population = create_initial_population()
population = evolve(population)