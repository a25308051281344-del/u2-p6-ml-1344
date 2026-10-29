import pandas as pd
import numpy as np 
# Hinojos Adrian NC:1344 
serie_amigos=["Pedro","Morgan","Nava","Eliseo","Mario","Jesse"]
print("---Serie listado de amigos NC:1344---")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes=[0,20,50,100.200,500,1000]
print("---Serie billetes MX NC:1344---")
billetes = pd.Series(serie_billetes)
print(billetes)

serie_billetes=[0,20,50,100.200,500,1000]
serie_bletras=["veinte","cincuenta","cien","dosientos","quinientos","mil"]
print("---Serie listado nombre y valor del billete MX NC:1344---")
tablabilletes= pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)

#diccionarios dataframe
#diccionario valor de monedas y nombre
print("---diccionario de dataframe en pandas NC:1344---")
dic_moedas={"serie_billetes":[0,20,50,100.200,500,1000],
            "serie_bletras":["veinte","cincuenta","cien","dosientos","quinientos","mil"]
}

tablabilletes=pd.DataFrame(dic_moedas, index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio")




