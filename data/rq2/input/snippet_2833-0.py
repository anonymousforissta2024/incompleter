def gnome_sort(alist):
    for pos in range(1, len(alist)):
        while pos != 0 and alist[pos] < alist[pos - 1]:
            alist[pos], alist[pos - 1] = (alist[pos - 1], alist[pos])
            pos = pos - 1
alist = [int(x) for x in alist]
gnome_sort(alist)
print('Sorted list: ', end='')
print(alist)