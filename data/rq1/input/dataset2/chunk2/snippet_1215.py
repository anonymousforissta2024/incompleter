#Source: https://stackoverflow.com/questions/49890365/type-error-takes-1-positional-argument-but-4-were-given
tt = MySparseMatrix(int, 2, 2)
tt.set(0,0,11)
tt.set(0,1,5)
tt.set(1,0,2)
print(tt.get(0,1))
print("tt = ", tt)