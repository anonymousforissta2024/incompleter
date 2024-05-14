#Source: https://stackoverflow.com/questions/73453914/i-am-getting-this-error-if-l-2-0-typeerror-unsupported-operand-types
s = 'one two three four five six'
l = s.split()
i = 0
l1 = []
while i < len(l):
    if l % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i+1

output = ' '.join(l1)
print(output)