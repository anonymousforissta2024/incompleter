#Source: https://stackoverflow.com/questions/61599509/list-definition-typeerror
list = open('intro.txt').read().split()
alph = "abcdefgjklmn'opqrstuvwxyz"
alph = alph + alph.upper()
clean_list = list()