#Source: https://stackoverflow.com/questions/46933027/combined-numbers-to-given-sum-typeerror-type-object-is-not-subscriptable
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if len(numbers) == 0:
        return
    elif s == target:
        print("sum({})={}".format(partial, target))
        return
    else:
        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[:i] + numbers[i+1:]
            subset_sum(remaining, target, partial + [n])

s = [2, 4]
k = [22, 25, -11, 13, 58]
x = [100, 101, 23]
v = [77, 88, 99]

y = s+k+x+v

if __name__ == "__main__":
    subset_sum(y, 47)