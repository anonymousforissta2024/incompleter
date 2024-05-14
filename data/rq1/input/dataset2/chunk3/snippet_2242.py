#Source: https://stackoverflow.com/questions/54710756/python3-typeerror-numpy-float64-object-is-not-iterable
# creating odd list of K for KNN
myList = list(range(1,50))

# subsetting just the odd ones
neighbors = filter(lambda x: x % 2 != 0, myList)

# empty list that will hold cv scores
cv_scores = []

# perform 10-fold cross validation
for k in neighbors:
    knn = KNN(n_neighbors=k, n_jobs = 6, metric = 'minkowski', contamination = 0.05)
    scores = cross_val_score(knn, X_test, pred, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())

### Create Plot
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# changing to misclassification error
MSE = [1 - x for x in cv_scores]

# determining best k
optimal_k = neighbors[MSE.index(min(next(iter(MSE))))]
print ("The optimal K neighbors number is %d" % optimal_k)

# plot misclassification error vs k
plt.plot(neighbors, MSE, figsize = (20,12))
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()