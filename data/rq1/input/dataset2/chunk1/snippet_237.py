#Source: https://stackoverflow.com/questions/64641718/python-caching-typeerror-unhashable-type-dict
def memoize(func):
    """Store the results of the decorated function for fast lookup
    """

    # Store results in a dict that maps arguments to results
    cache = {}

    def wrapper(*args, **kwargs):
        # If these arguments haven't been seen before, call func() and store the result.
        if (args, kwargs) not in cache:        
            cache[(args, kwargs)] = func(*args, **kwargs)          
        return cache[(args, kwargs)]

    return wrapper

@memoize
def add(a, b):
    print('Sleeping...')
    return a + b

add(1, 2)