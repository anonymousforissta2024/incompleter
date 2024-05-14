#Source: https://stackoverflow.com/questions/49964078/trying-to-implement-a-lisp-program-on-python-error-builtins-typeerror-int-o
def s_sum(l):

    if l == []:
        return 0
    else:
       print(l[:])
       # print(s_sum(l[1:]))
       return l.append(sum_numbers(l[0])) + s_sum(l[1:])

def sum_numbers(l):
    if l == []:
        return 0
    elif type(l[0]) is int:
        return l[0] + sum_numbers(l[1:])
    elif isinstance( l[0], str ):
        return sum_numbers(l[1:])
    else:
        return sum_numbers(l[0]) + sum_numbers(l[1:])


#l = list(input().split())
l = [ [ 1, 'h', 1, 'e' ], [ 5, 'b', 9 ], [ 4, 'k'] ]
#print(l)
s_sum(l)