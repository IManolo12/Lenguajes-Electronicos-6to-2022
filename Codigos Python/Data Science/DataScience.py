#Incluyo las bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Guardo el dataset con un método de pandas en la variable df
df = pd.read_csv('celebrity_deaths_2016.csv', header=None)
pd.set_option("display.max.columns", None)

#Elimino 2 columnas innecesarias y remplazo valores nulos por cero
df = df.drop([6, 7],axis=1)
df = df.fillna(0)

codList = ["cancer"]
codDict = {}
# for i in df.values:
#     if cod != 0:
#         codDic = {}

#Guardo las enfermedades en una lista sin que se guarden 2 veces seguidas. También como hay varios tipos de cancer agrupé todos en uno
for i in df.values:
    age = i[3]
    cod = i[5]
    if cod != 0 and cod not in codList:
        if "cancer" not in cod: codList.append(cod)

#Las keys del diccionario van a tener los strings que se encuentren en la lista
codDict = {k: 0 for k in codList}

#Si se repite una enfermedad se le suma 1 al valor de esa enfermedad
for i in df.values:
    cod = i[5]
    for k in codDict.keys():
        if k == cod: codDict[k] += 1

#Ordeno las keys de menor a mayor teniendo en cuenta su valor
afterSortCodDict = dict(zip(codList, sorted(codDict.values())))
temp = 0
for y in afterSortCodDict.keys(): 
    temp += 1    

print(temp)


#Gráfico----Falta lograr mostrar un slice del diccionario de las keys con los mayores 5 valores
#afterSortCodDict = afterSortCodDict[295:308]
x2 = afterSortCodDict.keys()
y2 = afterSortCodDict.values() 
plt.bar(x2,y2, label='barra', color="blue")
plt.title('Barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.grid()
plt.show()
