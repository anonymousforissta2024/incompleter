#Source: https://stackoverflow.com/questions/56100786/why-does-adding-two-counters-with-timedelta-values-raise-a-typeerror
from collections import Counter
from datetime import timedelta
a = Counter(time=timedelta(microseconds=167242))
a + a