#Source: https://stackoverflow.com/questions/54472631/getting-typeerror-trying-to-sum-the-contents-of-a-file
ctn =0
myfile = open("lab3.txt")
lines = myfile.readlines
for item in myfile:
        ctn += item
print(int(ctn))