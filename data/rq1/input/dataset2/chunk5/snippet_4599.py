#Source: https://stackoverflow.com/questions/77385362/i-cant-sum-the-numbers-of-a-nested-loop-typeerror-float-object-cannot-be-in
values = [29, 24, 20, 28, 22, 22, 23]
average = sum(values) / len(values)

for single_value in values:
    values_subtraction_average = single_value - average
    # >>> 5.0, 0.0, -4.0, 4.0, -2.0, -2.0, -1.0.

    for item in range(values_subtraction_average):
        x = sum(float(item))