#Source: https://stackoverflow.com/questions/62237600/how-do-i-get-around-typeerror-input-expected-at-most-1-argument-got-2-in-line
print("Hello")
name = input("What is your name?")
age = int(input("What is your age?",name)) 
print("Thank you",name, "you have been registered an age of",int(age))