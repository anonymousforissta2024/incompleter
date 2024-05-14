#Source: https://stackoverflow.com/questions/30903813/cant-set-parent-using-gtk-in-python-typeerror-argument-parent-expected-gtk-wi
top = App()
top.connect("delete-event", Gtk.main_quit)
top.show_all()
Gtk.main()