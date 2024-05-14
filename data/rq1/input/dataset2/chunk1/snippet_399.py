#Source: https://stackoverflow.com/questions/50214624/nonetype-error-converting-opengl-script-from-py-to-exe-using-cx-freeze
import sys
from cx_Freeze import setup, Executable
#go to dir in cmd, run python setup.py build or; setup.py build... will create a folder build with name.exe
setup(
    name = "Cube",
    version = "1.1",
    description = "Cube",
    executables = [Executable("OwnCube.py", base = "Console")])