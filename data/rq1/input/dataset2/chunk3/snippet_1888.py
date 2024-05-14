#Source: https://stackoverflow.com/questions/47204175/lane-departure-warning-system-for-autonomous-driving-typeerror-expected-non-em
if x.size == 0:
    raise TypeError("expected non-empty vector for x")
if y.ndim < 1 or y.ndim > 2:
    raise TypeError("expected 1D or 2D array for y")