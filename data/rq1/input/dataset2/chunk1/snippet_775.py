#Source: https://stackoverflow.com/questions/64584856/python-exec-with-a-function-chain-producing-nameerror
def run_code():
  code = """
def foo():
  print('foo')
  return 1

def bar():
  print('bar calls foo')
  return 1 + foo()

result = bar()
"""

  exec(code, globals(), locals())
  print('Result: {}'.format(locals()['result']))

run_code()