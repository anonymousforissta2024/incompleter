#Source: https://stackoverflow.com/questions/56919286/function-call-with-np-ndarray-say-typeerror-missing-1-required-positional-argu
#coding:utf-8

import numpy as np

def rotate_roll (th):
  _rot_vec_roll = {
    { 1.,          0. ,         0.},
    { 0.,   np.cos(th), np.sin(th)},
    { 0., - np.sin(th), np.cos(th)}
  }
  return _rot_vec_roll

def rotate_pitch (th):
  _rot_vec_pitch = {
    {  np.cos(th),0. , np.sin(th)},
    {  0.,        1.,          0.},
    {- np.sin(th),1.,  np.cos(th)}
  }
  return _rot_vec_pitch

def rotate_yaw (th):
  _rot_vec_yaw = {
    {   np.cos(th), np.sin(th), 0.},
    { - np.sin(th), np.cos(th), 0.},
    {           0.,         0., 1.}
  }
  return _rot_vec_yaw

# R2 = A * R1 
# A = roll_vec * pitch_vec * yaw_vec

Vector = np.ndarray(shape=(1,3), dtype=np.float)

def rotate_rpy(posvec: Vector, rotvec: Vector) -> Vector :
  return np.dot(np.dot(np.dot (posvec, rotate_rpy(rotvec[0]) ), rotate_pitch(rotvec[1]) ), rotate_yaw(rotvec[2]))

mypose = np.ndarray(shape=(1,3), dtype=np.float)
mypose = np.array([3.0,1.0,1.0], dtype=float)

print(mypose)

base = np.pi / 6.0

rotateang = np.ndarray(shape=(1,3), dtype=np.float)
rotateang = np.array([base, base/2.0, base], dtype=float)

print(rotateang)

newpose = np.ndarray(shape=(1,3), dtype=np.float)
newpose = rotate_rpy(mypose, rotateang)#enbug
print(newpose);