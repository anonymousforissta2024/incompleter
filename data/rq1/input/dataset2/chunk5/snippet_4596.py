#Source: https://stackoverflow.com/questions/75006215/fix-the-error-typeerror-function-object-is-not-subscriptable-with-out-chan
empty_rlist = None


def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    def dispatch(message, value=None):
        if message == 'getitem':
            if value == 0:
                return first
            return rest('getitem', value - 1)
    return dispatch


def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)
    return dispatch, contents


def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def first(s):
    """Return the first element of a recursive list s."""
    return s('getitem', 0)

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s('getitem', 1)


my_list = make_mutable_rlist()[0]
for x in range(4):
    my_list['push_first'](x)

print(my_list("len"))