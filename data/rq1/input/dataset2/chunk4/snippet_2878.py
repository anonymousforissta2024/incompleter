#Source: https://stackoverflow.com/questions/72147577/python-gtk-3-24-attributeerror-type-object-gtk-has-no-attribute-builder
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('user_interface.glade')

class Manipulador(object):
    def __init__(self):
        self.entry = builder.get_object('entry')
        self.label = builder.get_object('label')

    def on_button_clicked(self, button):
        text = self.entry.get_text()
        self.label.set_text(text)

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

builder.connect_signals(Manipulador())
window = builder.get_object()
window.show_all()
Gtk.main()