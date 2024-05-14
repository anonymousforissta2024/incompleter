#Source: https://stackoverflow.com/questions/32247006/python-attributeerror-module-object-has-no-attribute-goslate
import goslate
gs = goslate.Goslate()
print(gs.translate('hello world', 'bn'))