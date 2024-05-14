#Source: https://stackoverflow.com/questions/62347145/how-to-resolve-typeerror-builtin-function-or-method-object-is-not-iterable-on
f = open(fileFirst,'r').readlines
sf = open(fileSecond,'r').readlines
result = difflib.HtmlDiff()
diff = result.make_file(ff, sf, fileFirst, fileSecond)