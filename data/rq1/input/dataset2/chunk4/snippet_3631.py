#Source: https://stackoverflow.com/questions/57766464/typeerror-ufunc-isnan-not-supported-when-trying-to-remove-nan-float-type
for k,v in d.items():
    if np.isnan(v[1]):
        d.pop(k)
print(d)