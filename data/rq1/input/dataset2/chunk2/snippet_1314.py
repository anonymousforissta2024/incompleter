#Source: https://stackoverflow.com/questions/30903813/cant-set-parent-using-gtk-in-python-typeerror-argument-parent-expected-gtk-wi
class Windows(Gtk.Window):
    def About(self):
        about = Gtk.Window(title="About")
        about.set_border_width(10)
        about.set_resizable(False)
        about.set_transient_for(__init__)