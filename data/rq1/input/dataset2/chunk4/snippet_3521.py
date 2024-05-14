#Source: https://stackoverflow.com/questions/77195885/pywinauto-menu-select-attributeerror
from pywinauto.application import Application

app = Application(backend="uia")
app.start(app_path)
dlg = app.window()
dlg.wait("visible")
dlg.print_control_identifiers()
dlg.menu_select("File->Exit")