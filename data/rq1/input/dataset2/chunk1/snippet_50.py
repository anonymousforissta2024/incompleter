#Source: https://stackoverflow.com/questions/63007486/pywinauto-typeerror-item-2-in-argtypes-passes-a-union-by-value-which-is-unsu
from pywinauto.application import Application
app = Application(backend="uia").start("thinkorswim.exe")