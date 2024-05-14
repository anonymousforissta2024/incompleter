#Source: https://stackoverflow.com/questions/73790830/typeerror-int-object-is-not-iterable-apperars-when-i-try-to-add-a-string-int
def calculate(string: str):
    allowed_symboles = "1234567890+-*$"
    symbole_sum = len(string)
    symbole_sum0 = 0

    for symbole in string:
        for lol in allowed_symboles:
            if symbole == lol:
                symbole_sum0 += 1

    if symbole_sum != symbole_sum0:
        return "400: Bad request"

    all_numbers = []
    pos_of_operators = []

    for x, num in zip(string, range(0, len(string))):
        if x != "+" and x != "-" and x != "*" and x != "$":
            all_numbers += x
        else:
            pos_of_operators += num

    print(all_numbers, pos_of_operators)

calculate("1231241+4234")