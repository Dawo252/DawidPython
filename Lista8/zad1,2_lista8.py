import pandas as pd
import numpy as np
import xlrd
import openpyxl

def kropka_1(df):
    p=df.groupby(['Rok']).agg({"Liczba":['sum']})
    print(p[(p[('Liczba','sum')] > 1000)])

def kropka_2(df):
    print(df[df['Imie']=="DAWID"])

def kropka_3(df):
    print(df.agg({'Liczba':['sum']}))

def kropka_4(df):
    p = df[(df[("Rok")] >= 2000 ) & (df[("Rok")] <= 2005 )]
    print(p.agg({"Liczba":['sum']}))

def kropka_5(df):
    p = df[(df[("Plec")] == "M")]
    r = df[(df[("Plec")] == "K")]
    print("chlopcy", p.agg({"Liczba":['sum']}))
    print("dziewczynki", r.agg({"Liczba":['sum']}))

#def kropka_6(df)

def kropka_7(df):
    c = df[df["Plec"] == "M"]
    c_ilosc = df[df["Plec"] == "M"].max()
    print(c[(c["Liczba"]== c_ilosc["Liczba"])])
    d = df[df["Plec"] == "K"]
    d_ilosc = df[df["Plec"] == "K"].max()
    print(d[(d["Liczba"]== d_ilosc["Liczba"])])


lista = pd.read_excel(pd.ExcelFile("imiona.xlsx"), "Arkusz1")
print(lista)
kropka_1(lista)
kropka_2(lista)
kropka_3(lista)
kropka_4(lista)
kropka_5(lista)
kropka_7(lista)
