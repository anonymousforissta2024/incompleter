fname = input('Enter file name: ')
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print('Number of words:')
print(num_words)