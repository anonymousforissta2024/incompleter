#Source: https://stackoverflow.com/questions/62131223/typeerror-cannot-unpack-non-iterable-nonetype-object-while-using-operator-packa
import operator

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return '<{0},{1}>'.format(self.x,self.y)


def distance(a,b):
    return abs((a.x-b.x)**2+(a.y-b.y)**2)**.5

def closest(points):
    n = len(points)
    if n<=1:
        print("invalid input")
    elif n==2:
        return (points[0],points[1])
    elif n==3:
        (a,b,c)=points
        ret = (a,b) if distance(a,b) < distance(b,c) else (a,c)
        ret = (ret[0],ret[1]) if distance(ret[0],ret[1])<distance(b,c) else (b,c)
    else:
        points = sorted(points,key=operator.attrgetter('x'))
        leftPoints = points[:n//2]
        rightPoints = points[n//2:]
        (left_a,left_b) = closest(leftPoints)
        (right_a,right_b) = closest(rightPoints)
        d = min(distance(left_a,left_b),distance(right_a,right_b))
        mid = (points[n//2].x+points[n//2+1].x)/2
        midRange = filter(lambda pt:pt.x >=mid-d and pt.x<=mid+d,points)
        midRange = sorted(midRange,key=operator.attrgetter('y'))
        ret = None
        localMin = None
        for i in range(len(midRange)):
            a = midRange[i]
            for j in range(i+1,len(midRange)):
                b = midRange[j]
                if(not ret)or (abs(a.y-b.y)<=d and distance(a,b)<localMin):
                    localMin= distance(a,c)
                    ret = (a,b)
        return ret
points =[Point(1,2),Point(0,0),Point(3,6),Point(4,7),Point(5,5),Point(8,4),Point(2,9),Point(4,5),Point(8,1),Point(4,3),Point(3,3)]
print(closest(points))