#Source: https://stackoverflow.com/questions/43671634/python-3-typeerror-string-indices-must-be-integers-conditional-statement
#function that accepts a string and calculates the number of upper case and lower case

def case_count(str):
    total_cap_cases = 0
    total_low_cases = 0
    for words in str:
        if str[words].isupper():
            total_cap_cases += 1
        elif words.islower():
            total_low_cases += 1
        else:
            pass

    print(total_cap_cases)
    print(total_low_cases)


str = "How Many upper and LOWER case lettters are in THIS senTence?"
case_count(str)