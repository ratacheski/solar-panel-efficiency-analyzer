# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dadosjoin_dia.csv")


plt.plot(df["POTENCIA"],df["RADIACAO"],'ro')
plt.show()
