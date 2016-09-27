from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])

#X = np.mat(X)
#y = np.mat(y)

print np.shape(X), np.shape(y)
clf = LinearDiscriminantAnalysis()
clf.fit(X, y.T)

print(clf.predict([[-0.8, -1]]))