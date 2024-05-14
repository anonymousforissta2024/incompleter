#Source: https://stackoverflow.com/questions/45292395/error-typeerror-unorderable-types-int-str
corpus = indexed_data.select(col("KeyIndex",str).cast("long"), "features").map(list)