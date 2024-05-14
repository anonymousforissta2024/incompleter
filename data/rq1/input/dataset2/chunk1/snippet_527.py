#Source: https://stackoverflow.com/questions/49668387/type-error-cannot-convert-the-series-to-class-float
gmap = gmplot.GoogleMapPlotter(rep_points['lat'][0], rep_points['long'][0], 11)
gmap.plot(df_min.lat, df_min.lng)
gmap.scatter(rep_points['lat'],rep_points['long'],c='aquamarine')
gmap.circle(rep_points['lat'],rep_points['long'], 100, color='yellow')  
gmap.draw("user001_clus_time.html")