#Source: https://stackoverflow.com/questions/40829486/extracting-the-longest-subsequence-from-a-list-cant-figure-out-the-typeerror
def subSequence(sequence):

    newSequence = [0]
    longest = [0]

    for x in range(0,len(sequence)):
        print("x is " +str(x)+"\n")
        if sequence[x] == sequence[0]:
            newSequence.append(sequence[x])

        elif sequence[x] > sequence[x-1]:
            print("sequence[x] = " +str(sequence[x]))
            print("sequence[x-1] = " +str(sequence[x-1]))
            newSequence.append(sequence[x])

        else:
            if longest <= newSequence:
                del longest[:]
                longest.append(newSequence[:])
                print("longest = "+str(longest))
                del newSequence[:]
                newSequence.append(sequence[x])
            else:
                del newSequence[:]

    return newSequence

mySequence = [1,2,3,2,5,6,7,2]
print(subSequence(mySequence))