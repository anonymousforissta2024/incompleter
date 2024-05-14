#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 
import os
from gi.repository import Gtk, Poppler

testFile = 'file://' + os.path.join(os.getcwd(), 'printTestPdf.pdf')
pdfDocument = Poppler.Document.new_from_file(testFile, None)

class Example(Gtk.Window):
    def __init__(self):
        super(Example, self).__init__()                
        self.init_ui()

    def init_ui(self):    
        self.set_title("Print Pdf Test")
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
        printOperation.connect('draw-page', self.on_printOperation_draw_page)
        printOperation.set_job_name('Print Pdf Test')
        printOperation.set_n_pages(pdfDocument.get_n_pages())
        printOperation.run(Gtk.PrintOperationAction.PRINT_DIALOG,
                           parent=self)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = context.get_cairo_context() # <-- THIS IS THE LINE
        page = pdfDocument.get_page(pageNo)
        page.render_for_printing(cr)

def main():            
    app = Example()
    Gtk.main()

if __name__ == "__main__":    
    main()