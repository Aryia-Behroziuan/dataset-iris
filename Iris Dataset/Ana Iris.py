#---Iris Dataset in Machine Learning AI---

#Importing Librarys Machine Learning
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Starting Programming Librarys Machine Learning
iris = datasets.load_iris()
iris.data.shape
print('--------------------------------------------------------------------')
print('Dataset iris:')
iris.feature_names
iris.data
print(iris)
print('--------------------------------------------------------------------')

iris.target_names

print('Data Frame iris Dataset:')
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df)
print('--------------------------------------------------------------------')

iris_df['target'] = iris.target
iris_df

pd.plotting.scatter_matrix(iris_df, c=iris.target, figsize=[11, 11], s=150)
#plt.show()

from sklearn import datasets
iris = datasets.load_iris()
x = iris.data[:, [2, 3]] #only use petal length and width
y = iris.target
plt.scatter(x[:,0],x[:,1], c=y)
#plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6, metric='minkowski',p=2)
x = iris.data
y = iris.target
knn.fit(x, y)

iris.data

#warning
xx = np.array([[5, 3, 1, 0.2]])
yy = knn.predict(xx)
print(yy)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=
0.3, random_state=42, stratify=iris.target)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)
y_predict

knn.score(x_test, y_test)

neighbors = np.arange(1, 30)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))
for i,k in enumerate(neighbors):
 knn_model = KNeighborsClassifier(n_neighbors=k)
 knn_model.fit(x_train, y_train)
 train_accuracy[i] = knn_model.score(x_train, y_train)
 test_accuracy[i] = knn_model.score(x_test, y_test)

#plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
#plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
#plt.legend()
#plt.xlabel('number of Neighbors')
#plt.ylabel('Accuracy')
#plt.show()

from sklearn.linear_model import LinearRegression
x = np.arange(1,10)
y= np.array([28, 25, 26, 31, 32, 29, 30, 35, 36])

import matplotlib.pyplot as plt
plt.scatter(x,y)
#plt.show()

x = x.reshape(-1,1)
y = y.reshape(-1,1)
reg = LinearRegression()
reg.fit(x,y)

yhat = reg.predict(x)

plt.scatter(x,y)
plt.plot(x,yhat)
#plt.show()






