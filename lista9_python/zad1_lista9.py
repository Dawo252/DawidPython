import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

lista= pd.read_excel(pd.ExcelFile('imiona.xlsx'), 'Arkusz1')

df = lista.groupby(['Rok']).agg({'Liczba':['sum']})

df.plot()
plt.legend()
plt.show()