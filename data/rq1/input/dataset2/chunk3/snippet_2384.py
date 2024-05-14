#Source: https://stackoverflow.com/questions/62407334/typeerror-missing-1-required-positional-argument
ingredient = Recipe.Recipe.addIngredients(ingredientName, ingredientSize, ingredientUnitOfMeasure, ingredientQuantity)
while on:
    menuSelection = int(input("Would you like to: \n1. Create a recipe\n2. View a recipe\n3. Update a recipe\n4. Delete a recipe\n5. Quit"))
    while menuSelection != 1 or 2 or 3 or 4 or 5:
        if menuSelection ==  5:
            on = False
        elif menuSelection == 1:
            recipeName = input("Please type in the name of the recipe: ")
            recipeName = Recipe.Recipe('\n' + recipeName)
            addIngredient = True
            while addIngredient:
                ingredientName = input("Please enter the name of your first ingredient: ")
                ingredientSize = input("Please enter the size of the ingredient: ")
                ingredientUnitOfMeasure = input("Please enter the unit of measurement. Grams, millilitres etc:")
                ingredientQuantity = input("Please enter the quantity of the ingredient:")
                ingredient = ''
                ingredient = Recipe.Recipe.addIngredients(ingredientName, ingredientSize, ingredientUnitOfMeasure, ingredientQuantity)
                continueAdding = True
                answer = input("Would you like to add another ingredient? Type yes or no.\n")
                while continueAdding:
                    if answer.lower() == 'y' or 'yes':
                        addIngredient = True
                        break
                    elif answer.lower() == 'n' or 'no':
                        addIngredient = False 
                        break  
                    else:
                        answer = input("Please type yes or no.")
                print("You have finished adding all of your ingredients.\n")
            print("You have added " + recipeName + " to the recipe database.")