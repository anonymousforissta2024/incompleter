#Source: https://stackoverflow.com/questions/54622842/typeerror-list-indices-must-be-integers-or-slices-not-cupy-core-core-ndarray
iou = polygon_iou_gpu(polys[i], polys[order[j + 1]])