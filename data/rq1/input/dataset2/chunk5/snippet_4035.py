#Source: https://stackoverflow.com/questions/54202579/type-error-when-trying-to-modify-values-using-loc
df.loc[df["d"] == "Unknown", "e"] = "Not Unknown!"