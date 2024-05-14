from collections import Counter
import re
words = re.findall('\\w+', text)
print(Counter(words).most_common(10))