#Source: https://stackoverflow.com/questions/64550556/picklingerror-could-not-serialize-object-typeerror-cant-pickle-jpype-jmeth
rr=rdd.take(10)
for i in range(10):
  x=convert1(rr[i])
  print(x)