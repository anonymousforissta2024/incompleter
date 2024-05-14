import itertools as it

def char_shortest_distancer(str1, char1):
    result = [len(str1)] * len(str1)
    prev_char = -len(str1)
    for i in it.chain(range(len(str1)), reversed(range(len(str1)))):
        if str1[i] == char1:
            prev_char = i
        result[i] = min(result[i], abs(i - prev_char))
    return result
chr1 = 'r'
print('Original string:', str1, ': Specified character:', chr1)
print(char_shortest_distancer(str1, chr1))
str1 = 'python exercises'
chr1 = 'e'
print('\nOriginal string:', str1, ': Specified character:', chr1)
print(char_shortest_distancer(str1, chr1))
str1 = 'JavaScript'
chr1 = 'S'
print('\nOriginal string:', str1, ': Specified character:', chr1)
print(char_shortest_distancer(str1, chr1))