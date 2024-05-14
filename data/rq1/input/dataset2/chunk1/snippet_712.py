#Source: https://stackoverflow.com/questions/39052266/groupby-python-typeerror-unorderable-types-tuple-str
testdf1=testdf.groupby(['BRAND'])['VAL-P1','VAL-P2'].sum()