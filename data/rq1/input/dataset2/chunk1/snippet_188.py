#Source: https://stackoverflow.com/questions/66775462/error-typeerror-a-bytes-like-object-is-required-not-int
oldfile = open("buscrash_diversion.uexp", "rb")
l = list(oldfile.read())
out = open("1", "wb")
for i in l:
    out.write(i)