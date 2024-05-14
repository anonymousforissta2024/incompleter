#Source: https://stackoverflow.com/questions/59262525/python-attributeerror-str-object-has-no-attribute-keys
import chart_studio.plotly as py
import pandas as pd

df = pd.read_csv('MS.csv')

data = [ dict(
       type = 'choropleth',
       locations = df['CODE'],
       z = df['MS'],
       text = df['COUNTRY'],
       colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
           [0.6,"rgb(00, 120, 245)"],[0.7,"rgb(06, 130, 247)"],[1,"rgb(255, 255, 259)"]],
       autocolorscale = False,
       reversescale = True,
       marker = dict(
           line = dict (
               color = 'rgb(180,180,180)',
               width = 0.5
           ) ),
       colorbar = dict(
           autotick = False,
           tickprefix = None,
           title = 'ASes'),
     ) ]

layout = dict(
   title = 'MS COUNTRY',
   geo = dict(
       showframe = False,
       showcoastlines = False,
       projection = dict(
           type = 'Mercator'
       )
   )
)

fig = dict( data=data, layout=layout )
py.plot( fig, validate=False, filename='d3-world-map' )