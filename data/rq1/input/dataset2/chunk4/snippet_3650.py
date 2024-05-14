#Source: https://stackoverflow.com/questions/53342647/attributeerror-int-object-has-no-attribute-popincrease
class city:
     def __init__(self,a,b,c):
         self.name=a
         self.state=b
         self.polpulation=c
     def display(self):
         print("anme of city ",self.name)
     def popincrease(self):
         self.polpulation+=self.polpulation/10

a=city("ddn","utt",10245)
a.display()

new_pop=a.polpulation.popincrease
print(new_pop) 