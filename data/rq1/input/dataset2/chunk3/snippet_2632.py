#Source: https://stackoverflow.com/questions/71376220/typeerror-cannot-unpack-non-iterable-float-object-in-centered-average-algorithm
def calc_centered_average(numbers):
    sorted_list = sorted(numbers)
    return sum(sorted_list[1:-1])/(len(numbers)-2)
    # return subnumbers, centered_average


numbers = [1, 4, 5, 6, 100]
sublist, cavg = calc_centered_average(numbers)
print(f"The centered average of {numbers} is {cavg} (based on {sublist}).")