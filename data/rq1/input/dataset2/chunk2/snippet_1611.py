#Source: https://stackoverflow.com/questions/64582633/typeerror-missing-required-positional-arguments-using-getattr
from testc import TestClass

args = 'earth,moon,mars'
d = {'key':'value'}    
#v = getattr(TestClass, 'test')(args, d) #how do I get this to work?
v = getattr(TestClass, 'test')("earth", "moon", "mars", d)
print(v)