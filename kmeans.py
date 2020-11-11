# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("dadosjoin_dia.csv")

dataset = np.array([df["POTENCIA"],df["RADIACAO"]])
dataset = dataset.transpose()
#plt.plot(df["POTENCIA"],df["RADIACAO"],'ro')

kmeans = KMeans(n_clusters= 2, init= 'k-means++', n_init= 10, max_iter= 300)

pred_y = kmeans.fit_predict(dataset)

plt.scatter(dataset[:,1], dataset[:,0], c = pred_y)
plt.grid()

plt.show()
