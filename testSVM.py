from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import preprocessing
import numpy as np
import SVM
import processData

## step 1: load data
print "step 1: load data..."
processData.createData()
dataSet = []
labels = []
testdata = np.loadtxt('./testdata_tmp')
#testdata = np.loadtxt('./testSet.txt')
row,col = np.shape(testdata)
print row, col

dataSet = np.mat(testdata[:,0:-1])
labels = np.mat(testdata[:,-1]).T

train_x_raw = dataSet[0:row/2, :]
train_y = labels[0:row/2]
test_x_raw = dataSet[row/2:row, :]
test_y = labels[row/2:row]

lda_dataSet = testdata[:,0:-1]
lda_labels  = testdata[:,-1]

lda_train_x_raw = lda_dataSet[0:row/2, :]
lda_train_y = lda_labels[0:row/2]
lda_test_x_raw  = lda_dataSet[row/2:row, :]
lda_test_y  = lda_labels[row/2:row]
'''
#---Z-Score---
train_x = preprocessing.scale(train_x_raw)
test_x  = preprocessing.scale(test_x_raw)

lda_train_x = preprocessing.scale(lda_train_x_raw)
lda_test_x  = preprocessing.scale(lda_test_x_raw)
'''
train_x = train_x_raw
test_x  = test_x_raw
#---sklearn.preprocessing.StandardScaler---
'''
scaler_svm = preprocessing.StandardScaler().fit(train_x_raw)
train_x = scaler_svm.transform(train_x_raw)
test_x  = scaler_svm.transform(test_x_raw)
'''
scaler_lda = preprocessing.StandardScaler().fit(lda_train_x_raw)
lda_train_x = preprocessing.scale(lda_train_x_raw)
lda_test_x  = preprocessing.scale(lda_test_x_raw)


swtType = 0

if swtType:
    
    print np.shape(train_x), np.shape(train_y), np.shape(test_x), np.shape(test_y)
    ## step 2: SVM training...
    print "step 2: training..."
    C = 8
    toler = 0.001
    maxIter = 300
    svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))
    
    ## step 3: SVM testing
    print "step 3: testing..."
    accuracy = SVM.testSVM(svmClassifier, test_x, test_y)
    
    ## step 4: show the result
    print "step 4: show the result..."    
    print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
    #SVM.showSVM(svmClassifier)
else:
    #--- LDA (Linear Discriminant Analysis)---
#    lda_train_x = np.array(lda_train_x)
#    lda_train_y = np.array(lda_train_y)
#    lda_test_x  = np.array(lda_test_x)
#    lda_test_y  = np.array(lda_test_y)
    
    print np.shape(lda_train_x), np.shape(lda_train_y)
    
    clf = LinearDiscriminantAnalysis()
#    clf.fit(lda_train_x, lda_train_y)
    clf.fit(lda_test_x, lda_test_y)    
    test_result = clf.predict(lda_test_x)   
#    print test_result
    num_error = 0
    len_pre   = len(test_result)
    for i in range(len_pre):
        if test_result[i] == lda_test_y[i]:
            continue
        else:
            num_error += 1
    
    print num_error
    print 1 - num_error/float(len_pre)
    
    
    
