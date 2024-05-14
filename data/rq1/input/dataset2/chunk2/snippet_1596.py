#Source: https://stackoverflow.com/questions/73015092/why-am-i-getting-type-error-on-list-but-it-works-on-list-append
text_to_list = list(text)
list_to_number = []
for letter in text_to_list:
    cipher_num = alphabet.index(letter)
    list_to_number.append(cipher_num)