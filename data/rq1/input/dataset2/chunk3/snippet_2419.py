#Source: https://stackoverflow.com/questions/72340707/python-namedtuple-attributeerror-tuple-object-has-no-attribute-end-pos
from collections import namedtuple

class Parser:
    Rule = namedtuple('Rule', ['lhs', 'rhs', 'dot_pos', 'start_pos', 'end_pos'])

    # __init__ ...