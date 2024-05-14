#Source: https://stackoverflow.com/questions/43549634/typeerror-str-object-is-not-callable-in-python-script
actions = ['add','rem','rmusr']
if sys.argv[1] in actions:
    sys.exit(sys.argv[1](db, usr))