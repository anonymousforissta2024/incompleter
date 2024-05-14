#Source: https://stackoverflow.com/questions/62977585/im-getting-a-error-when-i-run-my-setup-py-on-cx-freeze-typeerror-expected-str
import cx_Freeze
import sys
import pandas
import numpy

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("app.py", base=base, icon="myicon.ico")]

cx_Freeze.setup(
    name = "Correlation-Generator",
    options = {"build_exe": {"packages":["tkinter","pandas","numpy"], "include_files":["myicon.ico"]}},
    version = "0.01",
    description = "A GUI Application which takes in metrics for generating a correlation value",
    executables = executables
    )