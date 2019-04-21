# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:14:26 2019

@author: ramra
"""


#importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

#importing the Iris dataset with pandas

IrisData = datasets.load_iris()
df = pd.DataFrame(IrisData.data, columns = IrisData.feature_names)
IrisTarget = pd.DataFrame(IrisData.target, columns=['Target'])


df = pd.concat([df, IrisTarget], join='inner', axis = 1)
x = df.iloc[:, [1, 2, 3, 4]].values

#Finding the optimum number of clusters for k-means classification
wcss  = {}

for i in range(1, 10):
	kmeans = KMeans(n_clusters=i, random_state=0).fit(df)
	wcss [i] = kmeans.inertia_

print (wcss )

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(list(wcss.keys()), list(wcss.values()))
plt.xlabel("Number of cluster")
plt.ylabel("wcss")
plt.show()
fig.savefig('KmeansElbow.jpeg')