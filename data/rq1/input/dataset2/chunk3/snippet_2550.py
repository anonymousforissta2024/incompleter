#Source: https://stackoverflow.com/questions/21957653/typeerror-when-using-cxfreeze
import sys
from cx_Freeze import setup, Executable


exe = Executable(
    script = 'cornell7.py',
    targetName = 'cornell7.exe',
    packages = ['header2.py'],
    targetDir = 'executable_dir',
    includes = [    'urllib.request', 'socket', 'sys', 'string', 'threading', 'time','datetime'],
    copyDependentFiles = True
    )
setup(    name = 'cornell7.exe',
          executables = [exe]
     )