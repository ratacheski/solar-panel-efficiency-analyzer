import pandas as pd


tempo = pd.read_csv("tempo.csv")

dados = pd.read_csv("2006001HR.csv")


tempo = tempo[13272:]
dados = dados[:10008]


dadosjoin = pd.DataFrame(columns=["DATA", "POTENCIA", "RADIACAO", "TEMPERATURA", "P/R"])
dadosjoin_dia = pd.DataFrame(columns=["DATA", "POTENCIA", "RADIACAO", "TEMPERATURA", "P/R"])

for i in range(10008):
    RAD = tempo["RAD_GLO"][i+13272]
    if (RAD<0):
        RAD = 0
    if (RAD > 100):
        novalinha2 = {"DATA":dados["DATACOMUM"][i], "POTENCIA":dados["PATIVA"][i], "RADIACAO":RAD, "TEMPERATURA":tempo["TEM_INS"][i+13272], "R/P":(RAD/float(dados["PATIVA"][i]))}
        dadosjoin_dia = dadosjoin_dia.append(novalinha2, ignore_index = True) 
    
    novalinha = {"DATA":dados["DATACOMUM"][i], "POTENCIA":dados["PATIVA"][i], "RADIACAO":RAD, "TEMPERATURA":tempo["TEM_INS"][i+13272], "R/P":(RAD/float(dados["PATIVA"][i]))}
    #print(novalinha)
    dadosjoin = dadosjoin.append(novalinha, ignore_index = True) 


dadosjoin.to_csv("dadosjoin.csv")
dadosjoin_dia.to_csv("dadosjoin_dia.csv")

    
    

    
