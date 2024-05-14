#Source: https://stackoverflow.com/questions/56961270/geopandas-spatial-join-attributeerror-nonetype-object-has-no-attribute-bou
id_grid = gpd.sjoin(gdf, grid, how="inner", op='intersects')