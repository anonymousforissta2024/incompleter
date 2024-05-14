#Source: https://stackoverflow.com/questions/53139681/typeerror-kivy-weakproxy-weakproxy-object-is-not-callable-kivi
import kivy
import glob
from os import path
import tkinter as tk
from kivy.app import App
from tkinter import filedialog
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

kivy.require('1.9.0')

class FilesPanel(GridLayout):
    frames_list = ObjectProperty()

    def open_files(self):
        root = tk.Tk()
        root.withdraw()

        self.load_files(filedialog.askdirectory(parent=root,initialdir="/", title='Please select a directory'))

    def load_files(self, selected_folder):
        all_bin_files = glob.glob(path.join(selected_folder, '*.bin'))

        for bin_file in all_bin_files:
            self.frames_list.adapter.data.extend([bin_file])
            self.frames_list._trigger_reset_populate()


class BinsPlayerMain(GridLayout):
    pass


class Bins_PlayerApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = 'Bins Player'
        self.icon = 'BinsPlayer.ico'
        return BinsPlayerMain()


if __name__ == "__main__":
    Bins_PlayerApp().run()