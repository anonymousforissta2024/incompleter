#Source: https://stackoverflow.com/questions/68181312/typeerror-unsupported-operand-types-for-builtin-function-or-method-and
def solution(s):
 
    word = input("Enter Text:" ).lower()
    
    for i in range(0, len(s)):
        if s[i].isupper():
            word=input + '000001'
            
        word=input+braillecodes[asciicodes.index(s[i].lower())]
        
    return word
        
#The Alpha Lookup Table
asciicodes = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
braillecodes = [
'000000',
'100000',
'110000',
'100100',
'100110',
'100010',
'110100',
'110110',
'110010',
'010100',
'010110',
'101000',
'111000',
'101100',
'101110',
'101010',
'111100',
'111110',
'111010',
'011100',
'011110',
'101001',
'111001',
'010111',
'101101',
'101111',
'101011']


#Print 
print (solution('s'))