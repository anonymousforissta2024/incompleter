#Source: https://stackoverflow.com/questions/49932846/typeerror-unsupported-operand-types-for-list-and-int-when-using-dictio
alphanumero = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q',
17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z' }

inputlet = str(input("Enter letter to be encrypted: "))
try:
    print(alphanumero[inputlet])
except KeyError:
    letnum = [k for k, v in alphanumero.items() if v == inputlet[0]]
inputkey = str(input("Enter key letter: "))
try:
    print(alphanumero[inputkey])
except KeyError:
    keynum = [u for u, t in alphanumero.items() if t == inputkey[0]]
result = (letnum + keynum) % 26
print(result)