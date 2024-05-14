def change_cases(s):
    return (str(s).upper(), str(s).lower())
print('Original Characters:\n', chrars)
result = map(change_cases, chrars)
print('\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:')
print(set(result))