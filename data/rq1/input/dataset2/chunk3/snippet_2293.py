#Source: https://stackoverflow.com/questions/56321383/typeerror-int-object-is-not-callable-1
class Line:
    def __init__(self,coor1,coor2):
        self.coor1= coor1
        self.coor2= coor2
    def distance(self):
        print(((self.coor1[0]-self.coor2[0])**2(self.coor1[1]-self.coor2[1])**2)**0.5)
    def slope (self):
        print((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()