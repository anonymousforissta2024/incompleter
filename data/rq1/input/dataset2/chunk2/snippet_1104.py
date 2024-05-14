#Source: https://stackoverflow.com/questions/55427880/typeerror-unsupported-operand-types-for-map-and-list-with-pyspark
# Transform all features into a vector using VectorAssembler
numericCols = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
assemblerInputs = map(lambda c: c + "TypeError: unsupported operand type(s) for +: 'map' and 'list'", categoricalColumns) + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]