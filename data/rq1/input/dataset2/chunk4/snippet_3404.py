#Source: https://stackoverflow.com/questions/76024991/how-can-i-fix-type-error-int-object-is-not-iterable
import random
def main():
    list1 = []
    for count in range(100):
        number = random.randint(1,100)
        list1.append(number)
    for i in range(0,100,10):
        print(change_list(number)[i:i+9])
        print(dir(number))

        
def change_list(number):
    list1 = sorted(number)
    return list1

main()