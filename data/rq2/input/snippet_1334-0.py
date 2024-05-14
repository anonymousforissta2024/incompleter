from collections import Counter
import re
text = 'The Python Software Foundation (PSF) is a 501(c)(3) non-profit \ncorporation that holds the intellectual property rights behind\nthe Python programming language. We manage the open source licensing \nfor Python version 2.1 and later and own and protect the trademarks \nassociated with Python. We also run the North American PyCon conference \nannually, support other Python conferences around the world, and \nfund Python related development with our grants program and by funding \nspecial projects.'
print(Counter(words).most_common(10))