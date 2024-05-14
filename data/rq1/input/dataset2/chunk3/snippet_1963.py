#Source: https://stackoverflow.com/questions/68475030/data-type-error-while-appending-suffix-in-numpy-nd-array
x[x[:,0]=='B',0] = x[x[:,0]=='B',0] + 'V'