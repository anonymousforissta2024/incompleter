#Source: https://stackoverflow.com/questions/45906514/attribute-error-while-using-cx-freeze
import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\Vinayak Singla\\Appdata\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\Vinayak Singla\\Appdata\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("pong.py")]

cx_Freeze.setup(
    name="Pongy",
    options={"build_exe": {"packages":["pygame","sys","random","time"],"include_files":["boing.wav","out.wav"]}},
    executables = executables
)