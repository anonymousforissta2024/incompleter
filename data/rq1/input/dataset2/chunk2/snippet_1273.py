#Source: https://stackoverflow.com/questions/75872760/problem-in-class-to-identify-the-gender-of-a-word-attributeerror-gender-obje
variable1 = "Pedro"

class Gender:
    def __eq__(self, male, female):
        x= male.startswith("o")
        y= female.startswith("a")
        return x,y

gender = Gender()


if variable1 == gender.male:
    print(variable1, " is male")
else:
    print(variable1, " is female")