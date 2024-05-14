#Source: https://stackoverflow.com/questions/72087232/attributeerror-int-object-has-no-attribute-pop
fruits=('apple','banana', ['kiwi','grapes'])
fruits[1].pop()
fruits[1].append('rice')
print(fruits)