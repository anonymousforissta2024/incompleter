#Source: https://stackoverflow.com/questions/62960685/why-do-i-receive-error-typeerror-argument-of-type-name-is-not-iterable
class Person:
    def __init__(self):
        list = pd.read_csv("mycsv.csv")
        self.name = self.Name()

    class Name:
        def __init__(self):
            self.name = list(['Name'].str.lower())
            for i in list:
                pass
if __name__ == "__main__":
    
    person = Person()
    checking_name = str(input()).lower()
    list = person.name

    if(checking_name in list):
        print("Hit")