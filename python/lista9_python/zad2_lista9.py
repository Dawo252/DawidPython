import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

lista= pd.read_excel(pd.ExcelFile('imiona.xlsx'), 'Arkusz1')

df = lista.groupby(['Plec']).agg({'Liczba':['sum']})

wykres = df.plot.bar()
wykres.set_ylabel('Plec')
wykres.set_xlabel('Liczba')
wykres.legend()
plt.title('Ilosc dzieci z podzialem plec')
plt.show()