# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:40:46 2020

@author: paulo
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:53:23 2020

@author: paulo
"""

import pandas as pd

arquivo = 'A002'

data = pd.read_json(arquivo+".json")

data.set_index("DT_MEDICAO")
data.drop("VEN_DIR", inplace=True, axis=1)
data.drop("PRE_INS", inplace=True, axis=1)
data.drop("DC_NOME", inplace=True, axis=1)
data.drop("VL_LATITUDE", inplace=True, axis=1)
data.drop("PRE_MIN", inplace=True, axis=1)
data.drop("PRE_MAX", inplace=True, axis=1)
data.drop("VEN_VEL", inplace=True, axis=1)
data.drop("UF", inplace=True, axis=1)
data.drop("VEN_RAJ", inplace=True, axis=1)
data.drop("CD_ESTACAO", inplace=True, axis=1)
data.drop("UMD_MAX", inplace=True, axis=1)
data.drop("UMD_INS", inplace=True, axis=1)
data.drop("VL_LONGITUDE", inplace=True, axis=1)
data.drop("UMD_MIN", inplace=True, axis=1)
data.drop("PTO_INS", inplace=True, axis=1)
data.drop("PTO_MIN", inplace=True, axis=1)
data.drop("PTO_MAX", inplace=True, axis=1)

data['HR_MEDICAO'] = data['HR_MEDICAO']/10
data['TEM_MAX'] = data['TEM_MAX'].astype('float')
data['RAD_GLO'] = data['RAD_GLO'].astype('float')
data['TEM_INS'] = data['TEM_INS'].astype('float')
data['TEM_MIN'] = data['TEM_MIN'].astype('float')
#data.columns = ["COD", "DATA", "PATIVA", "PREATIVA", "IDMEDIDOR"]
#data.drop("COD", inplace=True, axis=1)
#data.set_index("DATA")


data.to_csv("tempo.csv")
