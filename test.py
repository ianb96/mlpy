import pandas as pd
import quandl
import math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('mlclasstest.data.txt')
full_data = df.astype(float).values.tolist()
#data = np.array(full_data).drop('label')
#random.shuffle(full_data)

#print()
X = []#np.array()
y = []
for i in range(len(full_data)):
    X.append(full_data[i][0])
    y.append(full_data[i][1])
#X = np.array([full_data[i] for i in range(0,len(full_data),2)])
#X.sort()
#y.sort()
X = np.array(X)
y = np.array(y)
print("x",X)
print("r",y)
X = X.reshape(-1, 1)

maxX = max(X)+1
#y.reshape(1,-1)
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#clf = 
clf = LinearRegression(n_jobs=-1)
clf.fit(X, y)
m = clf.coef_
b = clf.intercept_
print("m", m)
print("b", b)
gsData = [m*i+b for i in range(1, maxX)]
#df['x'].plot()
#df.plot()
#plt.Line2D(X,y)
plt.plot([i for i in range(1, maxX)], gsData, label="model")
plt.plot(X, y, label="data", ls="None", marker="*", ms=15)
plt.legend(loc=4)
#plt.xlabel('Date')
#plt.ylabel('Price')
plt.show()