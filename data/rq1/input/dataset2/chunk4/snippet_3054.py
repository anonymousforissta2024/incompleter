#Source: https://stackoverflow.com/questions/66487695/getting-nameerror-while-i-already-have-defined-the-name-classes
class Restaurants():
    """Practicing classes."""
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurantInfo(self):
        print("The restaurant's name is: "+name.title()+".")
        print("The restaurant's cuisine type is: "+cuisine.title()+".")
    
    def rOpen(self):
        print(name.title()+" is open 24/7.")

restaurant = Restaurants('habibi','fast food')
print(restaurant.name.title()+" is the name of our Restaurant.")
print("We serve "+restaurant.cuisine.title()+".")
restaurant.rOpen()