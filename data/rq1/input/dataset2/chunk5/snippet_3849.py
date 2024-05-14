#Source: https://stackoverflow.com/questions/43793648/typeerrorlist-indices-must-be-integers-or-slices-not-list
Volume = array[0][2] 
counter = 0
for i in array: 
    if Volume == array[i][2]: #<------ why is this line a problem? 
        counter += 1