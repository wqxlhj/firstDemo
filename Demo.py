from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import SVM
import processData
import pandas as pd

## step 1: load data
print "step 1: load data..."
processData.createData()
dataSet = []
labels = []
testdata = np.loadtxt('./testdata_tmp')
print np.shape(testdata)