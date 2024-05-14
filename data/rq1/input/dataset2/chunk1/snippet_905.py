#Source: https://stackoverflow.com/questions/61211424/python-cx-freeze-filenotfounderror-errno-2-in-library-zip
from cx_Freeze import setup, Executable
includefiles = ['table.csv']
zipincludes = ['table.csv']
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files = includefiles, zip_includes = zipincludes)
include_package_data=True
base = 'Console'

executables = [
    Executable('ReportGenerator.py', base=base, targetName = 'report_generator')
]

setup(
    name='test13',
    version = '1.0',
    description = 'test13',
    options = dict(build_exe = buildOptions),
    executables = executables)