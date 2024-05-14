#Source: https://stackoverflow.com/questions/53308766/bokehgetting-typeerror-object-of-type-polygon-is-not-json-serializable
import shapefile
import itertools

shp = open("/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.shp", "rb")
dbf = open("/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.dbf", "rb")
sf = shapefile.Reader(shp=shp, dbf=dbf)

lats = []
lons = []
ct_name = []
st_id = []
ct_state_name = []
for shprec in sf.shapeRecords():
    st_id.append(int(shprec.record[0]))
    ct_name.append(shprec.record[5])
    ct_state_name.append(shprec.record[4])
    lat, lon = map(list, zip(*shprec.shape.points))
    indices = shprec.shape.parts.tolist()
    lat = [lat[i:j] + [float('NaN')] for i, j in zip(indices, indices[1:]+[None])]
    lon = [lon[i:j] + [float('NaN')] for i, j in zip(indices, indices[1:]+[None])]
    lat = list(itertools.chain.from_iterable(lat))
    lon = list(itertools.chain.from_iterable(lon))
    lats.append(lat)
    lons.append(lon)

map_data = pd.DataFrame({'x': lats, 'y': lons, 'state': st_id, 'county_name': ct_name, 'ct_state_name': ct_state_name})
map_data_m = map_data[map_data.ct_state_name.isin(['NJ'])]    

source = ColumnDataSource(map_data_m)

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="Title", tools=TOOLS,
           x_axis_location=None, y_axis_location=None)
p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color='color', fill_alpha=0.7,
          line_color="white", line_width=0.5)

show(p)