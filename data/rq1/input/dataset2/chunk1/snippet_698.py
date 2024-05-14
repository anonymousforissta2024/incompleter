#Source: https://stackoverflow.com/questions/50615169/typeerror-object-of-type-nonetype-has-no-len-after-using-remove-on-a-li
list_of_directions = ['right', 'left', 'up', 'down']
new_list = list_of_directions.remove('right')

print(len(new_list))