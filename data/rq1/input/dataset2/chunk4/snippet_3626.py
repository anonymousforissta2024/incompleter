#Source: https://stackoverflow.com/questions/74735553/osmnx-attributeerror-dataframe-object-has-no-attribute-crs
G = ox.graph_from_bbox(37.79, 37.78, -122.41, -122.43, network_type='drive')
G_projected = ox.project_graph(G)
ox.plot_graph(G_projected)