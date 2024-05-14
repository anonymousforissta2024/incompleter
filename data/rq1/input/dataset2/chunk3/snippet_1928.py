#Source: https://stackoverflow.com/questions/53145882/typeerror-kmeans-got-an-unexpected-keyword-argument-n-clusters
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


def KMeans():
    n = 4
    data = open("testSet.txt", "r")
    nums = []
    arr = np.empty((0,2), float)

    #Gets dataset from file
    for x in data.read().split(' '):
        nums.append(float(x))
    data.close()
    print(nums)

    #Stores numbers in a 2D array (X, Y axis)
    for x in range(0, len(nums), 2):
        arr = np.append(arr, np.array([[nums[x],nums[x+1]]]), axis=0)

    print(arr)

    kmeans = KMeans(n_clusters = 2).fit(arr)

    #Example 2, using make blobs to create random data
    X, y = make_blobs(n_samples=13, centers=5)
    print("Shape:", X.shape, y.shape)


    #Plotting the data
    plt.figure(0)
    plt.grid(True)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


    clf = KMeans(n_clusters=5)
    clf.fit(X)

    print(clf.labels_)

    z = clf.cluster_centers_
    print(z)


    plt.scatter(X[:,0], X[:,1], clf.labels_)
    plt.scatter(z[:,0],z[:,1], c='blue')
    plt.show()
KMeans()