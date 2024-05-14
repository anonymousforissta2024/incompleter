#Source: https://stackoverflow.com/questions/17093400/cx-freeze-yields-nameerror-name-build-exe-options-is-not-defined-on-build-a
import sys
from cx_Freeze import setup, Executable

setup(  name = "Duplicate Finder x86",
    version = "1.0",
    description = "Duplicate Finder x86",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Comparator Source.py", base=base)])