#Source: https://stackoverflow.com/questions/68013248/why-am-i-getting-typeerror-int-object-is-not-subscriptable
import math
import location
if __name__ == "__main__" :
    locationlist = []
    while True :
        try : 
            coordinate = input("Enter X and Y separated by a space, or enter a non-number to stop: ")
            x,y = coordinate.split()
            x = int(x)
            y = int(y)
            locationlist.append(coordinate)
        except ValueError :
            break
    print("Points: ",locationlist)
    location.where_is_xy(coordinate,locationlist)
    
if(len(locationlist)>=2):
    print("Distances:")
    for i in range(0,len(locationlist)-1):
        a=list(locationlist[i])
        b=list(locationlist[i+1])
        distance=math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        print(str(a)+" "+str(b)+" = "+str("%.2f" % round(distance, 2)))