#Source: https://stackoverflow.com/questions/70425953/attributeerror-tuple-object-has-no-attribute-lower-when-returning-specific
read_data = [] # stores Weather1, Weather2 etc. as we read that
final_array = [] # stores final arrays

# stores data for weather1, then clears it out and
# then stores data for weather2, and so on...
sub_array = [] 

# read each item of array
for x in array:

    # e.g. for first row, is Weather1 already read?
    # No, it's not read
    if x[0].lower() not in read_data:

        # when you reach weather 2 and hit this statement,
        # sub_array will have data from weather1. So, if you find
        # sub_array with data, it is time to add it to the final_array
        # and start fresh with the sub_array
        if len(sub_array) > 0:
            final_array.append(sub_array)
            sub_array = [x[2]]
        # if sub_array is empty, just add data to it
        else:
            sub_array.append(x[2])
        
        # make sure that read_data contains the item you read
        read_data.append(x[0].lower())

    # if weather1 has been read already, just add item to sub_array
    else:
        sub_array.append(x[2])

# After you are done reading all the lines, sub_array may have data in it
# if so, add to the final alrray
if len(sub_array) > 0:
    final_array.append(sub_array)