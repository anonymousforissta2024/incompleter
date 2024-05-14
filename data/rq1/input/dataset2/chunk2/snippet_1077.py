#Source: https://stackoverflow.com/questions/41498525/attribute-error-when-using-self
class search:
   def test(self):
      self.here = 'hi'
      self.gone = 'bye'
      self.num = 12

   def tester(self):
      return "{}".format(self.here)

s = search()
s.tester()
print (s.gone)