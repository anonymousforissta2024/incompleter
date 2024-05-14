#Source: https://stackoverflow.com/questions/50435311/program-is-not-working-typeerror-fit-missing-1-required-positional-argument
train=algo.fit(x,y)
res=train.pridict([test_setosa])
print(res)