#Source: https://stackoverflow.com/questions/61291553/getting-type-errorobject-of-type-nonetype-has-no-len-and-it-also-not-print
def reverse(seq):
    k=len(seq)

    for i in range(0,k):
        seq.append(seq.pop(i))
    print(seq)
reverse(reverse([1,2,3,4,5]))