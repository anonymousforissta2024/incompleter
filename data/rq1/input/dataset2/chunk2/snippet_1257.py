#Source: https://stackoverflow.com/questions/53612583/attempt-to-encrypt-a-text-file-causes-a-typeerror
my_text= F = open("mytext.txt")
KEY=4
encoded= ""

for c in my_text:
    rem = (ord(c) - 97 + KEY) % 26
    encoded += chr(rem + 97)

print(encoded)