#Source: https://stackoverflow.com/questions/35251749/nameerror-name-age-is-not-defined
def main():
    age = 0;
    weight = 0;
    birthMonth = " ";
    getAge();
    getWeight();
    getBirth();
    correct();

def getAge():
    age = input("Guess the age.\t")
    return age;
def getWeight():
    weight = input("Guess the weight.\t")
    return weight;
def getBirth():
    birthMonth = input("Guess the month.\t")
    return birthMonth;
def correct():
    if (age <= 25):
         print ("Congratulations, the age is 25 or less")
    else:
        print ("You did not correctly guess the age");
    if (weight <= 128):
        print ("Congratulations, the weight is 128 or more")
    else:
        print ("You did not correctly guess the weight");
    if (birthMonth == 25):
        print ("Congratulations, the month is April")
    else:
        print ("You did not correctly guess the month");
main();