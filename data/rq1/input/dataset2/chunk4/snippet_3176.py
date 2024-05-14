#Source: https://stackoverflow.com/questions/71909085/attributeerror-nonetype-object-has-no-attribute-find-in-python-collatz-con
import random

x = None
y = None
nru = None
nra = None
history = None
z = None
s = None
text1 = None
text2 = None
inpt = None

# Describe this function...
def func1():
  global x, y, nru, nra, history, z, s, text1, text2
  x = random.randint(1, 100)
  nru = x
  z = 2
  func4()

# Describe this function...
def func2():
  global x, y, nru, nra, history, z, s, text1, text2
  if x % 2 == 0:
    x = x / 2
  else:
    x = x * 3 + 1
  func3()

# Describe this function...
def func3():
  global x, y, nru, nra, history, z, s, text1, text2
  if x == 1:
    nra = nra + 1
    func1()
  else:
    if not history.find(y)+ 1 == 0:
      z = 3
      s = 'pending successful'
      func4()
    else:
      z = 1
      func4()

# Describe this function...
def func4():
  global x, y, nru, nra, history, z, s, text1, text2
  if z == 1:
    history = ''.join([str(x2) for x2 in [history, "'", x, "'"]])
    func2()
  elif z == 2:
    print(''.join([str(x3) for x3 in [text1, nru, text2, nra, s]]))
    func2()
  elif z == 3:
    nra = nra + 1
    print(''.join([str(x4) for x4 in [text1, nru, text2, nra, s]]))
    func5()


# Describe this function...
def func5():
  global x, y, nru, nra, history, z, s, text1, text2
  print(history)
  inpt = input("flaw? y/n")
  if inpt == 'y':
    s = 'pending'
    nra = nra + 1
    func1()
  elif inpt == 'n':
    s = 'success'


x = 0
y = 0
z = 0
s = 'pending'
nra = 0
nru = 0
text1 = 'The number that is running'
text2 = 'Number of numbers that ran'
text2 = 0
inpt = '0'
func1()