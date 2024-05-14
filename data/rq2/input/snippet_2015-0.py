from itertools import chain
import random
print('The original list is : ' + str(test_list))
res = random.choice(list(chain.from_iterable(test_list)))
print('Random number from Matrix : ' + str(res))