#Source: https://stackoverflow.com/questions/57719844/how-to-fix-typeerror-nonetype-is-not-iterable
counter = 1000
while counter != 10000:
    digits = [int(x) for x in str(counter)]
    bigdigits = digits.sort(reverse = True)
    smalldigits = digits.sort()

    strbigdigs = [str(i) for i in bigdigits]
    bignum = int("".join(strbigdigs))

    strsmalldigs = [str(j) for j in smalldigits]
    smallnum = int("".join(smalldigits))

    partialanswer = bignum - smallnum
    print(partialanswer)