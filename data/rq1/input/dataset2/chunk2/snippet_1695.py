#Source: https://stackoverflow.com/questions/70557770/prettytable-if-lenself-rows-in-0-lencolumn-attributeerror-str-obje
from prettytable import *

table = PrettyTable

table.add_column("", "Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("", "Type", ["Electric Type", "Water Type", "Fire Type"])

print(table)