import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('celebrity_deaths_2016.csv', header=None)
pd.set_option("display.max.columns", None)

df = df.drop([6, 7],axis=1)
df = df.fillna(0)

codList = ["cancer"]
codDict = {}
# for i in df.values:
#     if cod != 0:
#         codDic = {}
for i in df.values:
    age = i[3]
    cod = i[5]
    if cod != 0 and cod not in codList:
        if "cancer" not in cod: codList.append(cod)

codDict = {k: 0 for k in codList}

for i in df.values:
    cod = i[5]
    for k in codDict.keys():
        if k == cod: codDict[k] += 1

afterSortCodDict = dict(zip(codList, sorted(codDict.values())))
temp = 0
for y in afterSortCodDict.keys(): 
    temp += 1    

print(temp)
#afterSortCodDict = afterSortCodDict[295:308]
x2 = afterSortCodDict.keys()
y2 = afterSortCodDict.values() 
plt.bar(x2,y2, label='barra', color="blue")
plt.title('Barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.grid()
plt.show()
