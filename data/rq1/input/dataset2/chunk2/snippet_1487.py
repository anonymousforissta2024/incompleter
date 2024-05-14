#Source: https://stackoverflow.com/questions/27876683/mac-os-x-urwid-attributeerror-selectableicon-object-has-no-attribute-select
# hellotest.py
import urwid

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()