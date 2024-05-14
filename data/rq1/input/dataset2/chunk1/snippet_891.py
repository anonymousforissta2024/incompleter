#Source: https://stackoverflow.com/questions/19854226/how-does-iter-work-its-giving-typeerror-iterv-w-v-must-be-callable
l = [1,2,3,4,5,6]
for val in iter(l, 4):
    print (val)