#Source: https://stackoverflow.com/questions/74009860/how-do-i-fix-nameerror-in-python-i-defined-a-variable-in-a-for-loop-and-when-i
lc = [data['time'], data['magnitude'], data['error']]

fs = fts.FeatureSpace(data = ['time', 'magnitude', 'error'])
features, values = fs.extract(*lc)

t = pd.DataFrame(features, values)
print(t)