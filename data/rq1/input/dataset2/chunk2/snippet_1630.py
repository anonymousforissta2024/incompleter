#Source: https://stackoverflow.com/questions/56514847/attributeerror-module-math-has-no-attribute-name
import math

tmpl="This {mod._name_} module defines the value of pie as  {mod.pi}"

print(tmpl.format(mod=math))