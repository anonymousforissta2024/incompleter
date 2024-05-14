from collections import Counter
color1 = ['red', 'orange', 'green', 'blue', 'white']
counter1 = Counter(color1)
counter2 = Counter(color2)
print('Color1-Color2: ', list(counter1 - counter2))
print('Color2-Color1: ', list(counter2 - counter1))