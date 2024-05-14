#Source: https://stackoverflow.com/questions/60902295/error-when-trying-to-override-init-typeerror-init-takes-1-positio
def main():
   child = Child(2, first=1)
   child.display()


class Base():

   def __init__(self, **kwargs):
       print(kwargs.get("first", "nice try"))


class Child(Base):

   def __init__(self, value, **kwargs):
       super().__init__(self, **kwargs)
       self.value = value

   def display(self):
       print(self.value)


main()