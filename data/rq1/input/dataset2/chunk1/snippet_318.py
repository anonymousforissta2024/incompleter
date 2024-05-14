#Source: https://stackoverflow.com/questions/54840271/why-do-i-get-nameerror-name-is-not-defined-with-exec
exec("import random")
exec("def f():\n\treturn random.randint(0, 10), random.randint(0, 10)")
locals()['f']()