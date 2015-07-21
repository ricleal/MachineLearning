'''
Created on Jun 13, 2015

@author: rhf
'''

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

# import some data to play with
iris = datasets.load_iris()

X = iris.data
y = iris.target  # response vector

# train
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print 'knn:', metrics.accuracy_score(y_test, y_pred)
