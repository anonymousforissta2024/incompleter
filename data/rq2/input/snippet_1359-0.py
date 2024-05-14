sample_names = list(filter(lambda el: el[0].isupper() and el[1:].islower(), sample_names))
print('Result:')
print(len(''.join(sample_names)))