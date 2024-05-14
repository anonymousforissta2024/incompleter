#Source: https://stackoverflow.com/questions/75955986/nameerror-name-number-is-not-defined-working-with-lists
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
crayons_count = [10, 5, 7, 8, 9, 2, 3]

for index, color in enumerate(colors):
    print(index, color)

for (color) in colors and (number) in crayons_count:
    print (color, number)