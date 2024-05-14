#Source: https://stackoverflow.com/questions/57125779/how-to-fix-typeerror-invalid-keyword-argument-for-sort
def compare_points( p, q ):
    if p[0] < q[0] or (p[0] == q[0] and p[1] < q[1]):
        return -1
    elif p[0] > q[0] or (p[0] == q[0] and p[1] > q[1]):
        return 1
    else:
        return 0

#print(compare_points( [1,3], [5,6])) # outputs -1
#print(compare_points( [1,3], [1,6])) # ouputs -1
#print(compare_points( [1,3], [1,3])) # outputs 0
#print(compare_points( [1,3], [0,3])) # outputs 1


L = [ [5,8], [5,2], [12, 3], [1,3], [10,2], [12,1], [12,3] ]
L.sort(cmp=compare_points)
print(L)