# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy import unique
from numpy import where
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation

df = pd.read_csv("dadosjoin_dia.csv")

dataset = np.array([df["POTENCIA"],df["RADIACAO"]])
dataset = dataset.transpose()
#plt.plot(df["POTENCIA"],df["RADIACAO"],'ro')

model = AffinityPropagation(damping=0.9, random_state= 0)

model.fit(dataset)

yhat = model.predict(dataset)

clusters = unique(yhat)

for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	plt.scatter(dataset[row_ix, 0], dataset[row_ix, 1])

plt.show()