import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing

vulndata = pd.read_csv("/Users/aklyussef/Projects/Python/PatchClassifier/dataset_smaller.csv")
print(vulndata.shape)
print(vulndata.head())

X = vulndata.drop('Class', axis=1)
y = vulndata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
#svclassifier = SVC(kernel='linear')
svclassifier = SVC(kernel='rbf', C=100)
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))