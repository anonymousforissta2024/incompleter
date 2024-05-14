#Source: https://stackoverflow.com/questions/60989557/typeerror-can-only-concatenate-str-not-float-to-str-when-there-is-no-float
for x in range(len(nums)):
    file = open("updates" + str(x) + ".txt", "a")
    data2 = '{"Percent":"' + \
            element[x] + '", "diff":"' + diff + '"}'
    text = json.dump(data2 + '\n', file)