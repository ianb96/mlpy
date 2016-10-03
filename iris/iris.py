import pandas as pd
import quandl
import math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import sklearn
import random
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('iris.data.txt')
#df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)


#df = full_data#[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']]
# #df['class'].replace()
# # Iris-setosa       0
# # Iris-versicolor   1
# # Iris-virginica    2

# print(df)
# print(df['sepal_width'])
# input()

type_col = 'class'
# df['label'] = df[type_col]

X=[]
y=[]
#X = np.array(df.drop([type_col],1))
for i in range(len(full_data)):
    X.append([])
    for j in range(5):
        if j==4:
            y.append(full_data[i][j])
        else:
            X[i].append(full_data[i][j])
#X = np.array([j for i in len(full_data[j for j in len(full_data)]])
X = preprocessing.scale(X)
#df.dropna(inplace=True)
#y = np.array(df[type_col])
#y = np.array([i for i in full_data[j for j in len(full_data)]])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)


# test_size = 0.2
# train_set = {0:[], 1:[], 2:[]}
# test_set = {0:[], 1:[], 2:[]}
# train_data = full_data[:-int(test_size*len(full_data))]
# test_data = full_data[-int(test_size*len(full_data)):]
# for i in train_data:
#     train_set[i[-1]].append(i[:-1]) 
# for i in test_data:
#     test_set[i[-1]].append(i[:-1])

#clf = sklearn.svm()
#classifier
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)
# clf.fit(train_data, train_set)
# acc = clf.score(test_data, test_set)
print(acc)

#df['x'].plot()
#df.plot()
#plt.Line2D(X,y)
#plt.plot([i for i in range(1, maxX)], gsData, label="model")
#plt.plot(X, y, label="data", ls="None", marker="*", ms=15)
#plt.legend(loc=4)
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.show()