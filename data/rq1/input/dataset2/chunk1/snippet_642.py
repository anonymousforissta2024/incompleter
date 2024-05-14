#Source: https://stackoverflow.com/questions/17431638/get-typeerror-dict-values-object-does-not-support-indexing-when-using-python
{names[i]:d.values()[i] for i in range(len(names))}