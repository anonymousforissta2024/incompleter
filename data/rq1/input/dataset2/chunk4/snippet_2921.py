#Source: https://stackoverflow.com/questions/75634197/attributeerror-module-pywebkit-has-no-attribute-webview
import gi, pywebkit, webview
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from pywebkit import *

class Main(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='Browser')

        self.set_border_width(10)
        self.set_size_request(200, 100)
        self.button = Gtk.Button(label='Go')
        self.button.connect('clicked', self.test)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)
        self.user_input = Gtk.Entry()
        self.user_input.set_text('https://')
        vbox.pack_start(self.user_input, expand=False, fill=False, padding=4)
        vbox.pack_start(self.button, expand=False, fill=False, padding=4)

        web = pywebkit.WebView()

    def test():
        add = self.user_input.get_text()
        web.open(self.user_input)

win = Main()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()