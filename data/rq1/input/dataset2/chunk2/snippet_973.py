#Source: https://stackoverflow.com/questions/56919286/function-call-with-np-ndarray-say-typeerror-missing-1-required-positional-argu
def rotate_rpy(posvec: Vector, rotvec: Vector) -> Vector :
  return np.dot(np.dot(np.dot (posvec, rotate_rpy(rotvec[0]) ), rotate_pitch(rotvec[1]) ), rotate_yaw(rotvec[2]))

newpose = rotate_rpy(mypose, rotateang)#enbug