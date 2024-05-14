#Source: https://stackoverflow.com/questions/41475703/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-find
foodDict = {}
foodList = bsObj.findAll("td")
for foodItem in foodList:
    print("foodItems: " +foodItem.getText())
    meal = foodItem.parent.parent.parent.find("h4").getText().lower()
    print("Meal: " +meal)
    diningHall = foodItem.parent.parent.parent.parent.parent.parent.find("h2").getText().lower()
    s = "-"
    seq = (meal, diningHall)
    mealAndHall = s.join(seq)
    foodDict[foodItem.getText().lower().strip()] = mealAndHall
    print(foodDict)