#Source: https://stackoverflow.com/questions/54457740/typeerror-nonetype-is-unsubscriptable-if-statement
print(type(hit)) #I was getting tuple now NoneType...
print(len(hit))  # Was getting 2 now unsubscriptable
print(float(hit[1])) # 100