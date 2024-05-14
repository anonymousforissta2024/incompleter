#Source: https://stackoverflow.com/questions/53586382/csv-file-and-typeerror-a-bytes-like-object
seat =[]
csvfile = open('coba.csv') 
seating = csv.reader(csvfile)
for line in seating:
    seat.append(line)

print("Buy seat ?")
answer_1 = input("Answer : ")
if (answer_1 == "yes"):
    answer_2 = input("Enter preferred seat: ")
    if (answer_2 == "A1"):
        row = 1
        column = 0
        seat[row][column] = "X"
        writer = csv.writer(open('coba.csv', 'wb'))
        writer.writerows(seat)
        for line in seat:
            print(' | '.join(line))