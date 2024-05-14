#Source: https://stackoverflow.com/questions/51712946/bad-number-of-pixels-type-error-when-rotating-skymap-using-healpy-rotator-rota
import numpy as np
import healpy as hp
from astropy.utils.data import download_file
from astropy. io import fits

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

theta_deg = 35 #degrees 

phi = 0
theta = np.radians(theta_deg) 
psi = 0

a11 = (cos(psi)*cos(theta)) - (cos(theta)*sin(phi)*sin(psi))
a12  = (cos(psi)*sin(phi)) + (cos(theta)*cos(phi)*sin(psi))
a13  = sin(psi)*sin(theta)
a21  = (-sin(psi)*cos(phi)) - (cos(theta)*sin(phi)*cos(psi))
a22  = (-sin(psi)*sin(phi)) + (cos(theta)*cos(phi)*cos(psi))
a23 = cos(psi)*sin(theta)
a31 = sin(theta)*sin(phi)
a32 =   -sin(theta)*cos(phi)
a33 = cos(theta)

euler_list = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
euler_array = np.asarray(euler_list)
euler_deg = np.degrees(euler_array)
euler = euler_deg.reshape((3,3))

url  = ('https://dcc.ligo.org/public/0145/T1700453/001/LALInference_v1.fits.gz')
filename = download_file(url, cache=True)

r = hp.rotator.Rotator(euler, deg = False, eulertype = 'ZXZ')

R = hp.rotator.Rotator.rotate_map(filename, euler) #doesn't like this line