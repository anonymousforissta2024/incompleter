#Source: https://stackoverflow.com/questions/40672396/attributeerror-module-urwid-has-no-attribute-text
import urwid
txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()