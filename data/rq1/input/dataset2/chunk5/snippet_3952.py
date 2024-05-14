#Source: https://stackoverflow.com/questions/60880915/typeerror-int-object-is-not-subscriptable-is-being-shown-even-though-the-vari
def solution(l):
    if 1 in l:
        l.pop(l.index(1))
        k=[[min(l)]]
        l.pop(l.index(min(l)))
        for a in l:
            for index,i in enumerate(k):
                if a%i[0]==0:
                    k[index].append(a)
                else:
                    k.append(a)
        print(k)

solution([1, 2, 3, 4, 5, 6])