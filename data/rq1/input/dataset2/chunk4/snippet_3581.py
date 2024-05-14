#Source: https://stackoverflow.com/questions/71484368/typeerror-data-type-category-not-understood-while-looping-through-the-column
for col in data.columns:
    if data[col].dtype == "category":
        print(data[col].value_counts())
        print("\n\n")