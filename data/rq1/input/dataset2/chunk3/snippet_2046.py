#Source: https://stackoverflow.com/questions/67186716/attributeerrorfloat-object-has-no-attribute-log-typeerror-ufunc-log-not-su
ln2_4M = []
for x in df["2.4M"]:
    ln2_4M = np.log(x)
    print(ln2_4M)