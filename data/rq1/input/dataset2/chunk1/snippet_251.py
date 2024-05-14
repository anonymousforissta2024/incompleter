#Source: https://stackoverflow.com/questions/32943002/python-3-x-attributeerror-str-object-has-no-attribute-append
def enc(input, output, seq, str_int):
     input = input.lower()
     output = []
     for char in input:
         num = ord(char) + 5
         str_int = str(num)
         output.append(str_int)
         output = seq.join(output)
     return output
print(enc("hello", [], ' ', ' '))