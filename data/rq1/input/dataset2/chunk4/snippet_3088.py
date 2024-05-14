#Source: https://stackoverflow.com/questions/75518119/typeerror-restaurant-takes-no-arguments
class Restaurant():

    def __int__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is opened.")

restaurant = Restaurant('monarch', 'russian cuisine')
print(f"{restaurant.restaurant_name.title()} is the best restaurant of {restaurant.cuisine_type} in Moscow.")
restaurant.describe_restaurant()
restaurant.open_restaurant()