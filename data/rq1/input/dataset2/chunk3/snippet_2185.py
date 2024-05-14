#Source: https://stackoverflow.com/questions/70946230/need-to-filter-some-strings-elements-but-i-get-typeerror-unsupported-operand-ty
# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
bdegree = df[(df["education"] == "Bachelors") & (df["salary"] >= "50K")].count()
mdegree = df[(df["education"] == "Masters") & (df["salary"] >= "50K")].count()
phddegree = df[(df["education"] == "Doctorate") & (df["salary"] >= "50K")].count()
all_degrees = bdegree + mdegree + phddegree
print(all_degrees)
percentaje_of_more50 = (all_degrees / df["education" == "Bachelors"|"Masters"|"Doctorate"].count())*100
print("The percentaje of people with bla bla bla is", percentaje_of_more50["education"].round(1))