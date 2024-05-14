#Source: https://stackoverflow.com/questions/62876544/functools-reduce-gives-typeerror-int-object-is-not-subscriptable
total_population = functools.reduce(lambda a, b: a[0] + b[0], mid_points)