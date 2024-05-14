#Source: https://stackoverflow.com/questions/53651955/nameerror-name-is-not-defined-a-variable-defined-if-a-conditon-is-met
def collect_data(text):
    for line in text:
        key, match = parse_lines(line) #here I am parsing using a dict and regular expressions

        if key == something_1:
            var1 = match.group(1)
            list1.append(var1)

        elif key == something_2:
            var2 = match.group(2)
            list2.append(var2)

        elif key == something_3:
            func()

def func():
    for element in elements :
        if element == element1:
            variation = float(var1)
        elif element == element2:
            variation = float(var2)

         #here I append the variable variation to a list depending on the element name e.g. somelist.append(variation)
collect_data(text)