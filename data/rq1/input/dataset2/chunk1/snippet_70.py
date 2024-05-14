#Source: https://stackoverflow.com/questions/43054217/typeerror-dataframe-objects-are-mutable-thus-they-cannot-be-hashed-while-s
In [25]: h.sort_index(h.sort_values('age'))