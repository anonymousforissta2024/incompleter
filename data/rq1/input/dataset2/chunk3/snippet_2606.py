#Source: https://stackoverflow.com/questions/59422448/with-file-openr-encoding-utf-8-as-f-attributeerror-str-object-has-no-a
import pathlib
import lxml.etree as etree
from lxml.builder import ElementMaker
import functools
import operator

# Extract the name
cwd = pathlib.Path.cwd()
dirs = list(filter(lambda d: d.is_dir(), cwd.iterdir()))
langs = [dir_.name for dir_ in dirs]
files = map(operator.methodcaller('glob', '*.xml'), dirs)
files = map(lambda d: list(map(lambda f: f.with_suffix('').with_suffix('').name, d)), files)
filenames = set(functools.reduce(operator.add, files))

#print(langs)
#print(filenames)

# I will add the names of the files to the identifiers
identifiers = dict()

for file in filenames:
    with file.open('r',encoding="utf-8") as f:
        tree = etree.parse(file)
    root = tree.getroot()
    identifiers[filename] = root
    print(list(root.tag))