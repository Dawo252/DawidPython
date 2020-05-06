import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime

def kropka_1(df):
    p = df.Sprzedawca.unique()
    print(p)

def kropka_2(df):
    p = df.sort_values('Utarg', ascending=False)
    print(p.iloc[0:5])

def kropka_3(df):
    print(df.groupby(["Sprzedawca"]).agg({"Sprzedawca":["count"]}))

def kropka_4(df):
    print(df.groupby(["Kraj"]).agg({"Sprzedawca":["count"]}))

def kropka_5(df):
    p = (df[((df.Kraj=="Polska") &  (pd.DatetimeIndex(df['Data_zamowienia']).year==2005))])
    print(p.agg({"Sprzedawca":["count"]}))

def kropka_6(df):
    p = (df[(pd.DatetimeIndex(df['Data_zamowienia']).year==2005)])
    a = p.agg({"Utarg":["sum"]})
    b = p.agg({"Utarg":["count"]})
    print(a/b) #????
    
def kropka_7(df):
    p=df.copy()
    p['Rok']=pd.DatetimeIndex(p['Data_zamowienia']).year
    dwak4=p[p["Rok"]==2004].copy()
    dwak4=dwak4.drop(['Rok'],axis=1)
    dwak4.to_csv('zamowienia_rok2004.csv',header=True, index=False)
    dwak5=p[p["Rok"]==2005].copy()
    dwak5=dwak5.drop(['Rok'],axis=1)
    dwak5.to_csv('zamowienia_rok2005.csv',header=True, index=False)

lista= pd.read_csv("zamowienia.csv",header=0,delimiter=";")
print(lista)
kropka_1(lista)
kropka_2(lista)
kropka_3(lista)
kropka_4(lista)
kropka_5(lista)
kropka_6(lista)
kropka_7(lista)