#Source: https://stackoverflow.com/questions/66994103/python-checking-for-empty-list-on-a-path-subclass-is-returning-attributeerror
print(all([p.test and type(p) is WalkPath for p in paths]))
# prints True