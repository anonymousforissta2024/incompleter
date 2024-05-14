#Source: https://stackoverflow.com/questions/41372601/program-error-typeerror-not-all-arguments-converted-during-string-formatting
num = input('Please choose a number between 2 and 9:')
prime = True 

for test in range(2,10):

    if num % test == 0 and num != test:
        print(num,'equals',test, 'x', num/test)
        prime = False

if prime:
    print(num, 'is a prime number!')
else:
    print(num, 'is not a prime number!')