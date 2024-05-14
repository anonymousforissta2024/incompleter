def smallest_unit_length_intervals(points):
    """Return smallest set with unit-length intervals that includes all points.
 
    A smallest set containing closed intervals is returned such that each point
    is included in some interval.
    The intervals are in the form of tuples (a, b).
 
    points is a list of points on the x-axis.
    """
    points.sort()
    smallest_set = set()
    end_of_last_interval = float('-inf')
    for p in points:
        if end_of_last_interval <= p:
            interval = (p, p + 1)
            smallest_set.add(interval)
            end_of_last_interval = p + 1
    return smallest_set
points = [float(p) for p in points]
ans = smallest_unit_length_intervals(points)
print('A smallest-size set containing unit-length intervals that contain all of these points is', ans)