#Source: https://stackoverflow.com/questions/33628446/recalling-a-list-inside-another-list-python-typeerror-unhashable-type-list
lista_solic = {"name1" : "Full Name 1",
               "name2" : "Full Name 2",
               "name3" : "Full Name 3" } 
list_bcsulc = ["name1", "name2", "name3"]
list_sol = [lista_solic[list_bcsulc]]