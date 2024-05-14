#Source: https://stackoverflow.com/questions/51813378/attributeerror-worker-object-has-no-attribute-idf
w_dist = {} 
for w in workers: 
  f_dist = {} 
  for f in fences: 
     if f != self: 
        distance = self.rect_distance(w.rect, f.rect) 
        f_dist[f.idf] = distance 
  w_dist[w.idw] = f_dist 