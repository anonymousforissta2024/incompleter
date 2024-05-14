#Source: https://stackoverflow.com/questions/64987146/typeerror-int-object-is-not-subscriptable-in-python3-8
Alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

message = 'cöimamiçknsyznhaczstş'
for i in range(len(message)):
    message = Alphabet.index(message[i])