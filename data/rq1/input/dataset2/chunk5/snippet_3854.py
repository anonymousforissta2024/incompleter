#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 

import os
from gi.repository import Gtk
from weasyprint import HTML

testFile = os.path.join(os.getcwd(), 'printTestHtml.html')
pdfDocument = HTML(filename=testFile).render()

class Example(Gtk.Window):
    def __init__(self):
        super(Example, self).__init__()           
        self.init_ui()

    def init_ui(self):    
        self.set_title("Print Html Test")
        self.resize(230, 150)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)           
        printButton = Gtk.Button('Press Me')
        self.add(printButton)
        printButton.connect('clicked', self.on_printButton_clicked)
        self.show_all()

    def on_printButton_clicked(self, widget):
        """
        Handler for the button click.
        """            
        printOperation = Gtk.PrintOperation()
        printOperation.connect('begin-print', self.on_printOperation_begin_print)
        printOperation.connect('draw-page', self.on_printOperation_draw_page)
        printOperation.set_job_name('Print HTML Test')
        printOperation.set_n_pages(len(pdfDocument.pages))
        printOperation.run(Gtk.PrintOperationAction.PRINT_DIALOG,
                           parent=self)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = context.get_cairo_context() # <-- THIS IS THE LINE
        page = pdfDocument.pages[pageNo]
        page.paint(cr) # <-- there is a separate issue here

def main():        
    app = Example()
    Gtk.main()

if __name__ == "__main__":    
    main()