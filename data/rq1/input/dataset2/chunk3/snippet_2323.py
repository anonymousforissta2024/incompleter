#Source: https://stackoverflow.com/questions/57733732/what-is-the-reason-i-am-getting-a-nameerror-name-int-to-roman-is-not-defined
class Roman_Number():
    roman_numeral_table = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
    ]


    r = input('If you want to go from Roman to Number, enter "1." If you want to go from Number to Roman, enter "2"')

    if r == 1:
        roman_to_int()
    else:
        int_to_roman()

    def int_to_roman():
        number = int(input('Provide Number: '))
        if number < 1 or number > 3999:
            print('Number must be inbetween 1 and 3999')
        else:
            print('Valid Number')

        roman_numerals = []
        for numeral, value in roman_numeral_table:
            while value <= number:
                number -= value
                roman_numerals.append(numeral)

        print(''.join(roman_numerals))

        def roman_to_int():
            pass