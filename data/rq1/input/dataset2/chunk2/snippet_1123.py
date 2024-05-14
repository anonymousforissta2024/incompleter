#Source: https://stackoverflow.com/questions/43549634/typeerror-str-object-is-not-callable-in-python-script
if sys.argv[1] == 'add':
    sys.exit(add(db, usr))
if sys.argv[1] == 'rem':
    sys.exit(rem(db, usr))
if sys.argv[1] == 'rmusr':
    sys.exit(rmusr(db, usr))