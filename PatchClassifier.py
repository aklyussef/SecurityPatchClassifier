import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
from sklearn.metrics.scorer import make_scorer
from sklearn import preprocessing

vulndata = pd.read_csv("/Users/aklyussef/Projects/Python/PatchClassifier/dataset_smaller.csv")
print(vulndata.shape)
print(vulndata.head())

X = vulndata.drop('Class', axis=1)
y = vulndata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
#svclassifier = SVC(kernel='linear')
svclassifier = SVC(kernel='rbf', C=100000)
scoring = {'prec_macro': 'precision_macro','rec_micro': make_scorer(recall_score, average='macro')}
scores = cross_validate(svclassifier,X,y,scoring=scoring,cv=10,return_train_score=True)
print("Training Metrics")
print('|Iteration|Precision|Recall|')
for i in range(0,10):
    print('|{}|{}|{}|'.format(i,scores['train_prec_macro'][i],scores['train_rec_micro'][i]))
print("Testing Metrics")
print('|Iteration|Precision|Recall|')
for i in range(0,10):
    print('|{}|{}|{}|'.format(i,scores['test_prec_macro'][i],scores['test_rec_micro'][i]))