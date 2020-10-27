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

