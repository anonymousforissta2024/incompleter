#Source: https://stackoverflow.com/questions/56951307/math-sqrt-results-in-typeerrorfloat-object-cannot-be-interpreted-as-an-intege
pd = Power()
num = pd.calc_num()
cir_num = int(math.sqrt(num))**2
circles = []
filled = 0
while True:
    for i in range(math.sqrt(cir_num)-1):
        for j in range(math.sqrt(cir_num)-1):
            c = Circle(frame, cir_num)
            circles.append(c)
    ##drawing
    for c in circles:
        if c.stage == 'empty':
            c.draw_empty()
        elif c.stage == 'filled':
            c.draw_filled()
    avar = 0
    for c in circles:
        avar += c.num2
    filled += avar