#Source: https://stackoverflow.com/questions/61776922/python-3-exec-method-nameerror-name-of-a-defined-function-is-not-defined
filename = "./vir.py"
vir_globals = { "uc": 42, "cs": 12, "cycleOffset": -1 }

with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")

exec(code, vir_globals, {} )

print( 'exec: globals.cycleOffset', vir_globals['cycleOffset'] )