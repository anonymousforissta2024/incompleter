def bigram_sequence(text_lst):
    result = [a for ls in text_lst for a in zip(ls.split(' ')[:-1], ls.split(' ')[1:])]
    return result
print('Original list:')
print(text)
print('\nBigram sequence of the said list:')
print(bigram_sequence(text))