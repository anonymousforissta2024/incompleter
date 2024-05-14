#Source: https://stackoverflow.com/questions/56938663/trouble-changing-text-of-kivy-textinput-widget-using-id-raises-error-attribut
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
import nibabel as nib
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file("stack-test2.kv")

class Tabs(TabbedPanel):

    def nOpen(self):
        npop = niiPop()
        npop.open()

class niiPop(Popup):

    pathVariable = ' '
    file = ' '

    def nProcessor(self):
        if len(self.ids.nFile.selection) == 1:
            niiPop.pathVariable = str(self.ids.nFile.selection[0])
            niiPop.file = nib.load(niiPop.pathVariable)
            displayHeader = TextInput(text = str(niiPop.file.header), readonly = True)
            self.ids.nFile.clear_widgets()
            self.ids.nFile.add_widget(displayHeader)
            niiPop.auto_dismiss = True
            self.ids.fld1.text = niiPop.pathVariable
        else:
            self.ids.nFile.filename = ''

class stackTest1(App):
    def build(self):
        self.title = 'Test app'
        return Tabs()

if __name__ == "__main__":
    app = stackTest1()
    app.run()