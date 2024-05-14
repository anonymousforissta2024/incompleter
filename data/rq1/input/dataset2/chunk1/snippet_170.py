#Source: https://stackoverflow.com/questions/40513144/open-geotiff-with-gdal-produces-attributeerror-exit
with gdal.Open(filename) as gtiff:
    prj = gtiff.GetProjection()