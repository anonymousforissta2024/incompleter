#Source: https://stackoverflow.com/questions/48071947/why-is-my-enclosed-area-function-giving-typeerror-unsupported-operand-types
#First helping function: FIND POINTS OF INTERSECTION
#---------------------------------------------------------------------
#This function takes four int or float values representing two lines 
#and returns the x value of the point of intersection of the two lines. 
#If the lines are parallel, or identical, the function should return 
#None. 
#---------------------------------------------------------------------

def f(m1,b1,m2,b2):

    if m1 == m2:  
        return None

    else:
        return (b2 - b1)/(m1 - m2)   



#Second helping function: FIND LENGTH (DISTANCE BETWEEN POINTS)
#--------------------------------------------------------------------
#This function takes four int or float values representing two points 
#and returns the distance between those points.
#--------------------------------------------------------------------

def dist(x1,y1,x2,y2):

    return 

    D = ((x1-x2)**2 + (y1-y2)**2)


#3RD Helping function:  FIND AREA ENCLOSED BY 3 LINES 
#-----------------------------------------------------------------
#This function takes three int or float values representing side 
#lengths of a triangle, and returns the area of that triangle using 
#Heron's formula
#-----------------------------------------------------------------    
def heron(D1,D2,D3): 

    p = (D1 + D2 + D3)*0.5    
    # where p is half the perimeter 
    area = (p*(p-D1)*(p-D2)*(p-D3))**0.5

    return area 



#Finally, the last function:
#-------------------------------------------------------------------
#This function makes use of the helping functions above and connects 
#everything together 
#-------------------------------------------------------------------

def func(m1,b1,m2,b2,m3,b3):

#Using 1st helping function:
#---------------------------
    x1  = f(m1, b1, m2, b2)
    x2  = f(m1, b1, m3, b3)
    x3  = f(m2, b2, m3, b3)

    #---

    y1 = m1*x1 + b1
    y2 = m2*x2 + b2
    y3 = m3*x3 + b3


 #Using 2nd helping function:
 #---------------------------

    D1 = dist(x1,y1,x2,y2)
    D2 = dist(x1,y1,x3,y3)
    D3 = dist(x2,y2,x3,y3)


#Using 3rd helping function:
#---------------------------
    return heron(D1,D2,D3)


print(func(0,20,-2,50,0.5,-10))