#Source: https://stackoverflow.com/questions/49933153/how-can-i-fix-this-typeerror-int-object-is-not-iterable-when-counting-the-alp
x=0
f=open('in_a.txt',encoding='utf-8')
for line in f:
    h = len(line)
    for i in h:
        if line =="a"or line == "A":
            x+=1
            continue
print("this documents have%d A or a characters"  %(x))