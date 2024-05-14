#Source: https://stackoverflow.com/questions/68922318/gwpy-package-gives-error-attributeerror-module-matplotlib-pyplot-has-no-att
import pandas as pd
import seaborn as sns
from scipy import signal

from gwpy.timeseries import TimeSeries
from gwpy.plot import Plot
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def get_tseries_from_file(file_name):
  t_data = np.load(file_name)
  tseries1 = TimeSeries(t_data[0,:], sample_rate=2048)
  tseries2 = TimeSeries(t_data[1,:], sample_rate=2048)
  tseries3 = TimeSeries(t_data[2,:], sample_rate=2048)
  return tseries1, tseries2, tseries3

def plot_tseries(t1, t2, t3):
  plot = Plot(t1, t2, t3, separate=True, sharex=True, figsize=[20, 12])
  ax = plot.gca()
  ax.set_xlim(0, 2)
  ax.set_xlabel('Time [s]')
  plt.show()
  
file_1 = root_dir + 'train/0/0/0/000a5b6e5c.npy'
  
tseries1, tseries2, tseries3 = get_tseries_from_file(file_1)

# Plotting the 3 TimeSeries
plot_tseries(tseries1, tseries2, tseries3)