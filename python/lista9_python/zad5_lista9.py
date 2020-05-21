import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

lista= pd.read_csv("zamowienia.csv",header=0,delimiter=";")

df = lista.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = df.plot.bar()
wykres.set_ylabel('Sprzedawcy')
wykres.set_xlabel('Ilosc')
wykres.legend()
plt.title('Ilosc zamowien po sprzedawcach')
plt.show()