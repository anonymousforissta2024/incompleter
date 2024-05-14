#Source: https://stackoverflow.com/questions/76069108/running-into-a-typeerror-can-only-concatenate-list-not-int-to-list-error
x = 1

for i, sub_list in enumerate(example_list[1:-1], start=1):
    for j, entry in enumerate(sub_list[1:-1][1:-1], start=2):
        if j > 1:
            example_list[j] = round((example_list[j] + x), 3)
        example_list[i][j] += 1
print(example_list)