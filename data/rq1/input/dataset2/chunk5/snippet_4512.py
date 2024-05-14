#Source: https://stackoverflow.com/questions/52786661/typeerror-in-string-requires-string-as-left-operand-not-float
exg = ["I love apple.", 
        "there are lots of health benefits of apple.", 
        "apple is especially hight in Vitamin C,", 
        "alos provide Vitamin A as a powerful antioxidant!"]


fruit_list = ["pear", "banana", "mongo", "blueberry", "kiwi", "apple", "orange"]

for j in range(0, len(exg)):
    sentence = exg[j]
    if any(word in sentence for word in fruit_list):
        print(sentence)