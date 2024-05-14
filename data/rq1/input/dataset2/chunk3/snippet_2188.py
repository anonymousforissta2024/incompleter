#Source: https://stackoverflow.com/questions/64043109/getting-typeerror-write-argument-must-be-str-not-list-when-trying-to-add-tex
with open("text1.txt", "r") as f1:
    t1 = f1.readlines()
with open("text2.txt", "r") as f2:
    t2 = f2.readlines()
t2.insert(2, t1)
with open("text2.txt", "w") as f2:
    f2.writelines(t2)