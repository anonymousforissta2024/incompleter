#Source: https://stackoverflow.com/questions/61038174/python3-nameerror-name-open-is-not-defined
class Contoller:

    ...

    def __del__(self):
        store = {}
        ...
        pickle.dump(store, open('data.p', 'wb'))    

class MyWindow(Gtk.Window):

    def __init__(self):
        ...
        self.controller = Contoller(self)
        ...
        self.connect("delete-event", self.quit)
        ...

    ...

    def quit(self, widget, event):
        del self.controller
        Gtk.main_quit()