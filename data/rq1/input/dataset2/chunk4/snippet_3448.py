#Source: https://stackoverflow.com/questions/68417215/typeerror-float-object-is-not
xfile = open('/Users/Documents/python/mbox-short.txt')
for line in xfile:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    xf = (line.rstrip())
    ## Start Counting Lines
    count = 0 
    for numlines in xf:
        count = count + 1
    ## total count of lines with value <<<< code works up to this point
    values = float(line[20:])
    print(values)
    for n in values:
        print(n) 