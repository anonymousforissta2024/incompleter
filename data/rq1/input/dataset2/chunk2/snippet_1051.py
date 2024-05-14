#Source: https://stackoverflow.com/questions/63729685/how-to-differentiate-between-unexpected-keyword-argument-and-missing-positional
try:
    test_method()
except TypeError(MissingPositionalArgument):
    do_something()
except TypeError(UnexpectedKeywordArgument):
    do_something_else()