#Source: https://stackoverflow.com/questions/61272588/typeerror-init-missing-2-required-positional-arguments-x-and-y-in-li
class base:
    def __init__(self,width,length,x,y):
        self.__width=width
        self.__length=length
        self.__x=x
        self.__y=y

    def area(self):
        return self.__width*self.__length

    def perimeter(self):
        return 2*(self.__width+self.__length)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

class circle(base):
    def __init__(self,radius,x,y):
      super(circle,self).__init__(x,y)
      self.radius=radius

    def area(self):
        return math.pi*pow(self.radius,2)

    def perimeter(self):
        return 2*math.pi*self.radius

class rectangle(base):
    def __init__(self,width,length,x,y):
      super(rectangle,self).__init__(width,length,x,y)

# Test function: 

cir=circle(3,1,2)
cir.area()