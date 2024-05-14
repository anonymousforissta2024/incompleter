#Source: https://stackoverflow.com/questions/50843421/attributeerror-module-json-has-no-attribute-load-python3-6
#!/usr/bin/env python3

import json;
print(json.__file__)
import sys;


#a = json.load('["foo", {"bar":["baz", null, 1.0, 2]}]')
#pprint(a);

#sys.exit();

from pprint import pprint;

with open('services.json') as f:
        data=json.load(f);

pprint(data);