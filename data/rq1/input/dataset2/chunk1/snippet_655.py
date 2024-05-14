#Source: https://stackoverflow.com/questions/54546868/how-to-fix-typeerror-must-be-real-number-not-str-error
from pysal.cg.kdtree import KDTree
from pysal.cg import RADIUS_EARTH_MILES

trees_xys = results_df[['latitude', 'longitude']].values
trees_tree = KDTree(trees_xys, distance_metric='Arc', radius=RADIUS_EARTH_MILES)