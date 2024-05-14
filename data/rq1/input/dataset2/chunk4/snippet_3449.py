#Source: https://stackoverflow.com/questions/68254841/compiling-python-with-py2exe-produces-errors-attributeerror-genericrdata-obj
setup(
    name="event",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    windows=[{'script': 'main.py'}],
)