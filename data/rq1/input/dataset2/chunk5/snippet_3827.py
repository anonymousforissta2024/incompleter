#Source: https://stackoverflow.com/questions/39893049/how-to-solve-typeerrortype-object-is-not-subscriptable-in-python
r= list[random.randrange(1,20,50)]  
L2= []
for item in r:
    t= basic_delay + 2*basic_jitter*item - basic_jitter
    L2.append(str(t))

for item in L2:
    file.write("%s\n" % item)