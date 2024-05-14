#Source: https://stackoverflow.com/questions/57480494/how-to-fix-nameerror-name-password-is-not-defined
#Displays what I have learnt so far : Variable assignment, comparision operators, arithmetic operators, value operators, logical operators,

print('Welcome')
print('Enter Username')
username = input()
if username == 'Evan' :
    print('Enter Password')
else:
    print('Wrong Username. Program terminated.')

if username == 'Evan' :
    password = input()
    if password == 'Great' :
        print('Additional identification confirmation required.')
    else:
        print('Wrong password. Program terminated.')

if password == 'Great':
    print('What is your age?')
    years = (27)
    age = int(input())
    if age < years :
        print('Seriously?')
    elif age > years :
        print('-_-"')
    else:
        age == years
        print('Welcome Evan!')

if age == years:
    print('Name one of the RGB colours.')
    rgb = 'Red' or 'Green' or 'Blue'
    colours = input()
    if colours == rgb :
        print('Good')
    else:
        print('Wrong Answer')

if age == years :
    print('Type Rock & Roll.')
    answer = 'Rock & Roll'
    ans = input()
if ans != answer :
    print('Learn to type.')
else:
    print('Good job!')

if age == years:
    print('Let me show you some math for entertainment :D')
result = '= '
print('2+2')
print(result + str(int(2+2)))
print('')
print('3 - 2')
print(result + str(int(3-2)))
print('')
print('2 x 2')
print(result + str(int(2*2)))
print('')
print('7 / 3')
print(7/3)
print('')
print('3 modulus 7')
print(result + str(int(3%7)))
print('')
print('2 exponent 10')
print(result + str(int(2**10)))
print('')
print('23 floor division 9')
print(result + str(int(23//9)))