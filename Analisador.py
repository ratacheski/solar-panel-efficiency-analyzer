# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:53:23 2020

@author: paulo
"""

import pandas as pd
import numpy as np

arquivo = '2006001'

data = pd.read_csv(arquivo+"new.csv")
#print(data['PATIVA'][0])

for i in range(len(data.values)-3):
    lista_valores = [data.values[i][2],data.values[i+1][2],data.values[i+2][2]
                     ,data.values[i+3][2]]
    media = np.mean(lista_valores)
    sd = np.std(lista_valores)
    if(data.values[i][2] < media -2*sd or data.values[i][2] > media +2*sd):
        data['PATIVA'][i] = media

    
data.to_csv(arquivo+"NO.csv")  
print("teste")
data["DATACOMUM"] = str(data['DATA']).split(":")[0]
for i in range(len(data.values)):
    data["DATACOMUM"][i] =  str(data['DATA'][i]).split(":")[0]
print(data.groupby(data['DATACOMUM']).mean())
data = data.groupby(data['DATACOMUM']).mean()
#data.columns = ["COD", "DATA", "PATIVA", "PREATIVA", "IDMEDIDOR"]
#data.drop("COD", inplace=True, axis=1)
#data.set_index("DATA")

data.to_csv(arquivo+"HR.csv")
