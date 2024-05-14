#Source: https://stackoverflow.com/questions/71607384/python-function-error-typeerror-tuple-indices-must-be-integers-or-slices-not
clusters = np.zeros((len(dataset),1))

def assign(centroids,dataset,clusters,k):
    numOfObject=len(dataset)
    #for every object in the dataset
    for i in range(numOfObject):
        X=dataset[i,1:-1]
        #find the closest centroid
        centroidOfX= -1
        distanceToClosestcentroids = np.Inf
        for y in range(k):
            
            currentcentroids=centroids[y,:]
            dist=distance(X,currentcentroids)
            if dist<distanceToClosestcentroids:
                #Found closer Centroid
                distanceToClosestcentroids= dist
                centroidOfX=y
        #assign to X its closest centroid
        clusters[i]=int(centroidOfX)


#assign((2.5),dataset,clusters,20)
assign((2,1),dataset,clusters,20)