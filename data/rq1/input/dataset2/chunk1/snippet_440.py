#Source: https://stackoverflow.com/questions/53233113/python-multiprocessing-typeerror-cannot-serialize-io-bufferedreader-object
with contextlib.closing(Pool(50)) as pool:

        pool.map(partial(crack, f=z_file), lines)