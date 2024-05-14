#Source: https://stackoverflow.com/questions/54387341/attributeerror-tuple-object-has-no-attribute-weight
class Apple:
    def __init__( self,w,c):
        self.weight=w
        self.color=c
        print("utworzono!")



ap1=(280,"red")
print(ap1)
print(ap1.weight)