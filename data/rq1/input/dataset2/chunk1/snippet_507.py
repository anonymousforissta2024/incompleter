#Source: https://stackoverflow.com/questions/28502774/typeerror-cmp-is-an-invalid-keyword-argument-for-this-function
def my_cmp(x,y):
    counter = lambda x, items: reduce(lambda a,b:a+b, [list(x).count(xx) for xx in items])
    tmp =  cmp(counter(x, [2,3,4,5]), counter(y, [2,3,4,5]))
    return tmp if tmp!=0 else cmp(len(x),len(y)) 

for i, t in enumerate([tmp[0] for tmp in sorted(zip(tracks, self.mapping[idx][track_selection[-1]].iloc[0]), cmp=my_cmp, key=lambda x:x[1])]):
    img[i,:len(t)] = t