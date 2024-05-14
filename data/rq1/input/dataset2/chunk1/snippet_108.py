#Source: https://stackoverflow.com/questions/40513144/open-geotiff-with-gdal-produces-attributeerror-exit
from osgeo import gdal
gtiff = gdal.Open(filename)
prj = gtiff.GetProjection()
# do some work