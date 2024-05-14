#Source: https://stackoverflow.com/questions/65300596/typeerror-type-object-is-not-subscriptable
#Lua in Python

class string:
    def find(stringVariable, stringValue):
        output = stringVariable.find(stringValue)
        return output

    def sub(stringVariable, indexValueStart, *indexValueEnd):
        indexValueStart = int[indexValueStart]
        indexValueEnd = int[indexValueEnd]
        output = stringVariable[indexValueStart:indexValueEnd]
        return output

    def gsub(stringVariable, stringIndex):
        stringN = stringVariable[:stringIndex] + stringVariable[stringIndex + 1:]
        return stringN
        #gsub is not finished yet

a = input()

b = string.find(a, "abc")

c = string.sub(a, b, 5)

print(c)