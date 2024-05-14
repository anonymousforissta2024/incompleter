#Source: https://stackoverflow.com/questions/56583458/matplotlib-is-now-giving-an-unknown-property-attributeerror-since-update-to-py
from astroplan import Observer, FixedTarget
import astropy.units as u
from astropy.time import Time
import matplotlib.pyplot as plt
from astroplan.plots import plot_sky
import numpy as np

time = Time('2015-06-16 12:00:00')
subaru = Observer.at_site('subaru')
vega = FixedTarget.from_name('Vega')
sunset_tonight = subaru.sun_set_time(time, which='nearest')
vega_rise = subaru.target_rise_time(time, vega) + 5*u.minute
start = np.max([sunset_tonight, vega_rise])


plot_sky(vega, subaru, start)  
plt.show()  