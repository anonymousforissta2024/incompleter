#Source: https://stackoverflow.com/questions/50089536/typeerror-integer-argument-expected-got-float-python3
import string

f = open('data/hamlet.txt', 'r')
text = f.read()

alphabet_freq = []

for c in string.ascii_lowercase :
    alphabet_freq.append(text.count(c) + text.count(c.upper()))

alphabet_freq_sum = 0

for _ in alphabet_freq :
    alphabet_freq_sum +=_

letter_frequency = []

for _ in alphabet_freq :
    letter_frequency.append(( _ / alphabet_freq_sum) * 100)

alphabets = list(string.ascii_lowercase)

letter_frequency_in_freq_order = []

for _ in letter_frequency :
    letter_frequency_in_freq_order.append(letter_frequency.pop(max(letter_frequency)))

print(letter_frequency_in_freq_order,letter_frequency)