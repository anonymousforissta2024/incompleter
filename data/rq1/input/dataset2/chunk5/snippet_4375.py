#Source: https://stackoverflow.com/questions/72255624/getting-nameerror-name-count-even-is-not-defined-when-trying-to-get-the-odd
count_odd=0
for select in [321,13,42,9785,20,33,834,903,22]:
    if select % 2 == 0:
       count_even=count_even + 1
    else:
        count_odd=  count_odd + 1
print(count_even)
print( count_odd)