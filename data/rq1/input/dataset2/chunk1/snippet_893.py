#Source: https://stackoverflow.com/questions/64550556/picklingerror-could-not-serialize-object-typeerror-cant-pickle-jpype-jmeth
details = rdd.flatMap(lambda row: convert1(row)).collect()