#Source: https://stackoverflow.com/questions/70542010/typeerror-bad-operand-type-for-abs-vpython-cyvector-vector
test_force(vector(0,0,0),vector(1,0,0),1,1,vector(1,0,0))    # distance = 1 in x direction
test_force(vector(1,0,0),vector(0,0,0),1,1,vector(-1,0,0))   # swap objects
test_force(vector(0,0,0),vector(2,0,0),1,1,vector(0.25,0,0)) # distance = 2
test_force(vector(0,0,0),vector(0,1,0),1,1,vector(0,1,0))    # distance = 1 in y direction
test_force(vector(10,0,0),vector(10,1,0),1,1,vector(0,1,0))  # displaced from origin
test_force(vector(0,0,0),vector(1,0,0),2,1,vector(2,0,0))    # non-unit mass 1
test_force(vector(0,0,0),vector(1,0,0),1,2,vector(2,0,0))    # non-unit mass 