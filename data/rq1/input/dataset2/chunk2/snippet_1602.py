#Source: https://stackoverflow.com/questions/41553652/type-error-when-using-sparkit-learns-sparkcountvectorizer
my_rdd2 = sc.parallelize(['some perfectly reasonable string', 'another perfectly reasonable string'])
array_rdd_2 = ArrayRDD(my_rdd2)
tf = counter.fit_transform(array_rdd2)
tf
# <class 'splearn.rdd.SparseRDD'> from PythonRDD[20] at RDD at PythonRDD.scala:48