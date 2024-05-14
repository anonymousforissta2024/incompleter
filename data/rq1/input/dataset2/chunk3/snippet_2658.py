#Source: https://stackoverflow.com/questions/64506532/attributeerror-nonetype-object-has-no-attribute-coords
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.coordinates import SkyCoord 
from astropy.coordinates import ICRS, Galactic, FK4, FK5  
from astropy.coordinates import Angle, Latitude, Longitude  
import astropy.units as u


filename = get_pkg_data_filename('jopi.fits')


hdu = fits.open(filename)[0]
wcs = WCS(hdu.header).celestial
wcs.wcs.crval = [0,0]
wcs.wcs.ctype = [ 'XOFFSET' , 'YOFFSET' ]


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(projection=wcs)
plt.imshow(hdu.data[0][0], origin='lower') 
lon = ax.coords[0]
lat = ax.coords[1]
lon.set_major_formatter('x')
lat.set_major_formatter('x')
lon.set_format_unit(u.milliarcsecond)
lat.set_format_unit(u.milliarcsecond)
ax.set_xlim(200,800)
ax.set_ylim(200,800)
ax.set_xlabel('Relative R.A ()')
ax.set_ylabel('Relative Dec ()')