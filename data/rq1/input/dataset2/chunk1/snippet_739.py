#Source: https://stackoverflow.com/questions/19877064/typeerror-unsupported-operand-types-for-dict-keys-and-list
_LEAST_GREATER_ODD = lambda x: (x + 1) | 1
_LEAST_GREATER_EVEN = lambda x: (x + 2) & ~1

X2_X5_MAPPINGS = {
    'RLE': (_LEAST_GREATER_ODD, 'N'),
    'LRE': (_LEAST_GREATER_EVEN, 'N'),
    'RLO': (_LEAST_GREATER_ODD, 'R'),
    'LRO': (_LEAST_GREATER_EVEN, 'L'),
}

# Added 'B' so X6 won't execute in that case and X8 will run its course
X6_IGNORED = X2_X5_MAPPINGS.keys() + ['BN', 'PDF', 'B']
X9_REMOVED = X2_X5_MAPPINGS.keys() + ['BN', 'PDF']