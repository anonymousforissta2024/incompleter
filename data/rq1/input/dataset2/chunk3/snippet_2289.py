#Source: https://stackoverflow.com/questions/50546057/nameerror-name-default-string-is-not-defined
class TripleString:

    # intended class constants

    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "(undefined)"


# constructor method

def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
            string3 = DEFAULT_STRING):

    # assigning default values to the variables first

    self.string1 = self.DEFAULT_STRING

    self.string2 = self.DEFAULT_STRING

    self.string3 = self.DEFAULT_STRING

    # setting values using setter methods,

    self.set_string1(string1)

    self.set_string2(string2)

    self.set_string3(string3)


# mutator ("set") methods

def set_string1(self, string1):
    if self.valid_string(string1):
        self.string1 = string1

        return True

    return False


def set_string2(self, string2):
    if self.valid_string(string2):
        self.string2 = string2

        return True

    return False


def set_string3(self, string3):
    if self.valid_string(string3):
        self.string3 = string3

        return True

    return False


# accessor ("get") methods

def get_string1(self):
    return self.string1


def get_string2(self):
    return self.string2


def get_string3(self):
    return self.string3


def to_string(self):
    return self.string1 + ", " + self.string2 + ", " + self.string3


# helper methods for entire class

def valid_string(self, the_str):
    if len(the_str) >= self.MIN_LEN and len(the_str) <= self.MAX_LEN:
        return True

    return False


# ------------- CLIENT --------------------------------------------------

# Create 4 TripleString objects and printing

triple_string_num_1 = TripleString()

print(triple_string_num_1.to_string())

triple_string_num_2 = TripleString("Alice")

print(triple_string_num_2.to_string())

triple_string_num_3 = TripleString("Bob", "Chris")

print(triple_string_num_3.to_string())

triple_string_num_4 = TripleString("Oliver", "Laurel", "Thea")

print(triple_string_num_4.to_string())

print("")

# mutating values using setter methods

triple_string_num_1.set_string1("Lance")

triple_string_num_2.set_string2("XYZ")

triple_string_num_3.set_string1("Bobby")

triple_string_num_4.set_string2("Felicity")

print(triple_string_num_1.to_string())

print(triple_string_num_2.to_string())

print(triple_string_num_3.to_string())

print(triple_string_num_4.to_string())

print("")

# testing if validation working properly

if triple_string_num_4.set_string2(""):

    print("successful in setting empty string for string2 of 4th object," + \
          "validation is not working properly")

else:

    print(
        "failed in setting empty string for string2 of 4th object," + \
        "validation is working properly")

    print("Value after setting: ", triple_string_num_4.get_string2())