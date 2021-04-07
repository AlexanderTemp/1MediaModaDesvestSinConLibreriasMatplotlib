# -*- coding: utf-8 -*-
"""
@author: Alexander Humberto Nina Pacajes
"""

import pandas as pd
import numpy as np
df = pd.read_csv('diabetes.csv')
while(True):
    print("Seleccione: ")
    print("---------------------------")
    print("1.- moda")
    print("2.- media")
    print("3.- desviacion estandar")
    print("4.- Terminar")
    print("--------------------------")
    
    op=int(input())
    if op==1:
        print("Moda de cada feature")
        for col in df.columns:
            print(col)
            print(df[col].mode())
        print('.................................')
    if op==2:
        print("Media de cada feature")
        for col in df.columns:
            print(col)
            print(round(df[col].mean(),3))
        print('.................................')
    if op==3:
        print("Desviacion Estandar de cada feature")
        for col in df.columns:
            print(col)
            print(round(df[col].std(),3))
        print('.................................')
    if op==4:
        break