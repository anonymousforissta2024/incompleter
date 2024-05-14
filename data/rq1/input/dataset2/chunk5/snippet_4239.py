#Source: https://stackoverflow.com/questions/46559020/typeerror-string-indices-must-be-integers-what-should-i-do-to-avoid-this-error
lat = []
lng = []
for x in sd:
    for y in sd:
        for z in y["geometry"]:
            lat.append(z["location"]["lat"])

for x in sd:
    for y in sd:
        for z in y["geometry"]:
            lng.append(z["location"]["lng"])

print(lat, lng)