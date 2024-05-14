#Source: https://stackoverflow.com/questions/54274101/holoviews-opts-for-plots-throwing-attributeerror
import pandas as pd
import holoviews as hv
from holoviews import opts
hv.extension('bokeh', 'matplotlib')
hv.notebook_extension('bokeh','matplotlib')

# Declaring data
filepath = 'somefilepath+somefile.csv'
df  = pd.read_csv(filepath, skipinitialspace = True, encoding = 'utf-8')
curves = hv.HoloMap({col: hv.Curve(df, 'Index', col) for col in df.columns},
               kdims='Column')

curves.opts(
    opts.Area(color='#fff8dc', line_width=2),
    opts.Curve(color='black'))