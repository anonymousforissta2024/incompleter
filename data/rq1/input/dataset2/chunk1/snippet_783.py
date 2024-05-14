#Source: https://stackoverflow.com/questions/48083149/nameerror-name-is-not-defined
finished = True

def number():
    x = int(input("Please enter a number \n"))
    m = x%2

if m>0:
    print("Odd")
    finished = True
else: 
    print("Even")
    finished = True

while finished:
    number()