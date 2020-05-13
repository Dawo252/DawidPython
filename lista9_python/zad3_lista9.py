import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

lista= pd.read_excel(pd.ExcelFile('imiona.xlsx'), 'Arkusz1')

df=lista.agg({"Rok":['max']})
df2=lista[(lista["Rok"]<= df.values[0][0])&(lista["Rok"]> df.values[0][0]-5)]
df3=df2.groupby(['Plec']).agg({'Liczba':['sum']})

wykres = df3.plot.pie(subplots = True, autopct = '%.2f %%', fontsize = 10, figsize = (6, 6))
plt.title('urodzone dzieci z podzialem na plec')
plt.show()