#Source: https://stackoverflow.com/questions/45113377/typeerror-when-calling-spark-mllib-logisticregressionwithlbfgs-train
trainingData = sXYdf.rdd.map(lambda x: reg.LabeledPoint(x[0]-1,x[1:]))
trainingData.take(2)