#Source: https://stackoverflow.com/questions/55469766/typeerror-list-object-is-not-callable-problem-with-passing-generated-array
import numpy as np
import math
import random
import operator

# Global variables
a = 0.1
b = 1


def function(x):
    return (math.sin(40*math.pi*x)+math.pow(x-1, 4))/(2*x)


def initial_pop():
    pop = np.random.uniform(a, b, 20)
    pop = pop.tolist()
    return pop


def moving_pop(population):
    # e c
    rand_item = population[random.randrange(len(population))]
    # print(rand_item)
    direction_arr = [-1, 1]
    direction = direction_arr[random.randrange(len(direction_arr))]
    # print(direction)
    new_element = rand_item + direction * np.random.normal(0, 0.2)
    if new_element > b:
        extra = new_element - b
        new_element = a + extra
    if new_element < a:
        extra = abs(new_element - a)
        new_element = b - extra
    # print(new_element)
    return new_element


def create_moved_pop(population):
    new_population = []
    for x in range(0, 20):
        new_element = moving_pop(population)
        new_population.append(new_element)
    # print(new_population)
    return new_population


def star_pop(population):
    random_item1 = population[random.randrange(len(population))]
    random_item2 = population[random.randrange(len(population))]
    while random_item2 == random_item1:
        random_item2 = population[random.randrange(len(population))]
    e_star = (random_item1 + random_item2)/2
    return e_star


def create_star_pop(population):
    star_population = []
    for x in range(0, 20):
        new_element = star_pop(population)
        star_population.append(new_element)
    # print(new_population)
    return star_population


pop = initial_pop()
print(pop)
for i in range(0, 500):
    moved_pop = create_moved_pop(pop)
    star_pop = create_star_pop(pop)
    pop_combined = sorted(sorted(pop) + sorted(moved_pop) +                 
sorted(star_pop))
    y_array = []
    for x in range(0, len(pop_combined)):
        y_array.append(function(pop_combined[x]))
    x_y_array = dict(zip(pop_combined, y_array))

    sorted_x_y_array = sorted(x_y_array.items(), key=operator.itemgetter(1), reverse=True)
    sorted_x_y_array = sorted_x_y_array[0:20]
    print(sorted_x_y_array)
    pop.clear()
    for x in sorted_x_y_array:
        pop.append(x[0])
    print(pop)