#Source: https://stackoverflow.com/questions/64863278/what-is-the-solution-to-this-type-error-list-indices-must-be-integers-or-slices
startX=random.randint(20,cellWidth)
startY=random.randint(20,cellHeight)
snakeCoords=[{"x":startX,"y":startY},
             {"x":startX-1,"y":startY},
             {"x":startX-2,"y":startY}]