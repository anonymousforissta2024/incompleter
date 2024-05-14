from collections import deque
import re
__operators__ = '+-/*'
__parenthesis__ = '()'

def test_higher_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]
print(test_higher_priority('*', '-'))
print(test_higher_priority('+', '-'))
print(test_higher_priority('+', '*'))
print(test_higher_priority('+', '/'))
print(test_higher_priority('*', '/'))