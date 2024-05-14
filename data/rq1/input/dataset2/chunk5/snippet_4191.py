#Source: https://stackoverflow.com/questions/61773112/attributeerror-tuple-object-has-no-attribute-asjson
if not filename or filename == '-':
    text = sys.stdin.read()
else:
    with open(filename) as f:
        text = f.read()

grammarname = 'grammars/CTEST.ebnf'
grammarData = open(grammarname).read()
parser = tatsu.compile(grammarData, asmodel=True)

model = parser.parse(text)
print()
print('# MODEL TYPE IS:', type(model).__name__)
print(json.dumps(model.asjson(), indent=4))
print()