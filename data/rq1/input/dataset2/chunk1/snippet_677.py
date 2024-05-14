#Source: https://stackoverflow.com/questions/34169770/typeerror-len-of-unsized-object-when-comparing-and-i-cannot-make-sense-of-it
In [2]: select_sens = sens[([lat_min]<=sens['LATITUDE']) & (sens['LATITUDE']<=[lat_max]) &
                           ([lon_min]<=sens['LONGITUDE']) & (sens['LONGITUDE']<=[lon_max])].copy()