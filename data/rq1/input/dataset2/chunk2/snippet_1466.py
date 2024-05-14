#Source: https://stackoverflow.com/questions/7081905/python-3-2-typeerror-unsupported-operandss-for-nonetype-and-str
my_name = 'Joe Bloggs'
my_age = 25
my_height = 71 # inches
my_weight = 203 #lbs approximate, converted from ~14.5 stones
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s") % my_name
print ("He's %d inches tall.") % my_height
print ("He's %d pounds heavy.") % my_weight
print ("Actually that's not too heavy")
print ("He's got %s eyes and %s hair.") % (my_eyes, my_hair)
print ("His teeth are usually %s depending on the coffee.") % my_teeth