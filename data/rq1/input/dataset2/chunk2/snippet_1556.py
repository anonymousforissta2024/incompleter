#Source: https://stackoverflow.com/questions/31685788/calling-sys-stderr-fileno-after-checking-it-is-a-python-callable-raises-an
if hasattr(sys.stderr, 'fileno'):
    if callable(sys.stderr.fileno):
       i = sys.stderr.fileno()