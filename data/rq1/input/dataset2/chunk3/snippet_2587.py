#Source: https://stackoverflow.com/questions/63046056/im-trying-to-print-a-list-it-gives-type-error
buyList = ["Potato", "Suger", "Rice", "Oil", "Cake", "Biscuit"]

for i in buyList:
    if i % 2 is not 0:
        print(i, end=" ")
        i += 1