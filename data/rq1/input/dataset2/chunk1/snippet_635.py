#Source: https://stackoverflow.com/questions/64863278/what-is-the-solution-to-this-type-error-list-indices-must-be-integers-or-slices
apple=randomlocation()
def randomlocation():
           return {"x":random.randint(20,cellWidth),
                   "y":random.randint(20,cellHeight)}