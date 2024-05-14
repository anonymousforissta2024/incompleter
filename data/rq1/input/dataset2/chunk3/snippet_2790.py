#Source: https://stackoverflow.com/questions/57921147/python-rolling-apply-gives-typeerror
def f(x):
    print(len(x)) 
    return

test.set_index('exchTstamp',inplace=True)
test['fit_x'].rolling('1.0S').apply(lambda x: f(list(x)))