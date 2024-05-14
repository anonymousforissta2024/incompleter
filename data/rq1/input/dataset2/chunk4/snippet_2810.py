#Source: https://stackoverflow.com/questions/69877663/how-to-fix-typeerror-vowels-missing-required-positional-argument-filehandl
def vowels(filehandle):
    num_vowel = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for c in filehandle:
        if c in vowels:
            num_vowel = num_vowel+1
    return num_vowel

def consonants(filehandle):
    num_con = 0
    for c in filehandle:
        if c >= 'a' and c <= 'z':
            if c not in vowels:
                num_con = num_con+1
        elif c>='A' and c<='Z':
            if c not in vowels:
                num_con = num_con+1
    return num_con

def case(filehandle):
    uppercase = 0
    lowercase = 0
    for c in filehandle:
        if c>='a' and c<='z':
            uppercase=uppercase+1
        elif c>='A' and c<= 'Z':
            lowercase=lowecase+1
    return uppercase, lowercase

def main():
    vowel = vowels()
    consonants = consonants()
    uppercase, lowercase = case()
    try:
        filename=input('Enter name of text file: ')
        filehandle=open('words.txt', 'r')

        print('Vowels:', vowels)
        print('Consonants:', consonants)
        print('Uppercase:', uppercase)
        print('Lowercase:', lowercase)

        filehandle.close()
    except IOError:
        print('FILE NOT FOUND')


main()