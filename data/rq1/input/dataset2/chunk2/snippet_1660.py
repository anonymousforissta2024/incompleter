#Source: https://stackoverflow.com/questions/61573953/attributeerror-list-object-has-no-attribute-startswith
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

for city_m in cities:
    if cities.startswith("M"):
        print("Cities that start with M:", cities)
    else:
        print("No cities start with M.")