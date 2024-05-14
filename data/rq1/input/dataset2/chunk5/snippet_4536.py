#Source: https://stackoverflow.com/questions/49355749/how-to-fix-typeerror-input-expected-at-most-1-arguments-but-got-3
def leg_count(w):
    x = input("How many legs does a", w, "have? ")
    print("A", w, "has", x, "legs")

leg_count("crocodile")