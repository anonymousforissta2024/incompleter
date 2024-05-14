#Source: https://stackoverflow.com/questions/54564583/how-to-fix-typeerror-must-be-real-number-not-numpy-str-occurred-at-inde
radius_in_miles = 0.5

def get_complaint_count(r):
    xy = r['latitude'], r['longitude']
    distances, indices = trees_tree.query(xy, k=trees_count, distance_upper_bound=radius_in_miles)
    indices = indices[~np.isnan(indices)]
    return len(indices)

treeLocations['# of Complaints within 0.5 miles'] = treeLocations.apply(get_complaint_count,axis=1)

treeLocations