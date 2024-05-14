#Source: https://stackoverflow.com/questions/63065061/why-do-i-get-attributeerror-when-i-run-this-code
from collections import Counter
import re
  

s = open( 'filename.txt', 'r')
words = re.findall('\w+', s.lower())
c = Counter(words)

for word, freq in c.most_common(10):
    print(word, ':' , freq)