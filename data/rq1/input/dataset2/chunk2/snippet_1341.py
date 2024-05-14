#Source: https://stackoverflow.com/questions/53933467/program-shows-typeerror-while-passing-a-dictionary-into-a-function-argument
def f(**kwargs):
   print(kwargs)

d = {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}   
f(**d)   # {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}

d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}   
f(**d)   # TypeError: f() keywords must be strings