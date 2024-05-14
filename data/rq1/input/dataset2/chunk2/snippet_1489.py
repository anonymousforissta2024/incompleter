#Source: https://stackoverflow.com/questions/49762189/keep-getting-name-error-name-getname-not-defined
class Pet :

    def main() :
        print(getName())
        print(getSpecies())
        print(getAge())

    def getName(self) :
        name = str(input("What is your pets name: "))
        return name

    def getSpecies(self) :
        species = str(input("What is your pets species: "))
        return species

    def getAge(self) :
        age = int(input("Please type in your age: "))
        return print(age)

    main()