#Source: https://stackoverflow.com/questions/8613515/python3-porting-typeerror-unorderable-types-dict-int
for v in vertices:
    if dist[v.node_id] < min_dist:
        min_dist = dist[v.node_id]
        cur_min = v