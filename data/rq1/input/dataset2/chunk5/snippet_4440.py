#Source: https://stackoverflow.com/questions/42047047/how-can-i-get-around-the-nonetype-error-in-python
wordset = rRWords("master.txt")
if len(wordset) == 80000 and type(wordset) is set:
    print("Well done Lucy Success!")
else:
    print("Not good Lucy Failed")    