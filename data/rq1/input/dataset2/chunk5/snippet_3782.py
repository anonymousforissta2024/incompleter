#Source: https://stackoverflow.com/questions/40505484/typeerror-int-object-is-not-subscriptable-adding-to-a-tuple-in-a-loop
GeneratedX = []
x = (200,1)
y = (168,1)
GeneratedX.append(x)
GeneratedX.append(y)
i = True
while i == True:
    for current in GeneratedX:
        GeneratedX = (current[0],current[1] + 1)
        print(GeneratedX)