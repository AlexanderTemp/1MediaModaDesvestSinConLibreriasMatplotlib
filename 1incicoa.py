# -*- coding: utf-8 -*-
"""
@author: Alexander Humberto Nina Pacajes
"""
import csv
import math
ds_dia = "diabetes.csv"
nom_col = []
filas = []
with open(ds_dia, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    nom_col = next(csvreader)
    for row in csvreader:
        filas.append(row)
def moda():
    print('----------------------------------------------')
    print('1.- Moda de Cada Feature')
    print('----------------------------------------------')
    for nom in range(len(nom_col)):
        print(str(nom_col[nom])+'\t', end=' ')
    print()
    list1=[]
    for i in range(len(nom_col)):
        listaux=[]
        for j in range(len(filas)):
            listaux.append(filas[j][i])
        listaux.sort()
        j=0
        List=[]
        while j<len(listaux):
            List.append(listaux.count(listaux[j]))
            j+=1
        d1=dict(zip(listaux, List))
        d2={k for (k,v) in d1.items() if v == max(List)}
        list1.append(d2)
    for lis in list1:
        print(str(lis)+'\t', end='')
    print('----------------------------------------------')
def media():
    print('----------------------------------------------')
    print('2.- Media de Cada Feature')
    print('----------------------------------------------')
    for nom in range(len(nom_col)):
        print(str(nom_col[nom])+'\t', end=' ')
    print()
    list1=[]
    for i in range(len(nom_col)):
        listaux=0
        for j in range(len(filas)):
            listaux+=float(filas[j][i])
        list1.append(round(listaux/len(filas),3))
    for lis in list1:
        print(str(lis)+'\t', end='')  
    print('----------------------------------------------')
def desvest():
    print('----------------------------------------------')
    print('3.- Desviación Estandar de Cada Feature')
    print('----------------------------------------------')
    for nom in range(len(nom_col)):
        print(str(nom_col[nom])+'\t', end=' ')
    print()
    list1=[]
    for i in range(len(nom_col)):
        listaux=0
        for j in range(len(filas)):
            listaux+=float(filas[j][i])
        media=round(listaux/len(filas),3)
        det=0
        for j in range(len(filas)):
            det+=((float(filas[j][i])-media)*(float(filas[j][i])-media))
        list1.append(round(math.sqrt(det/len(filas)),3))
    for lis in list1:
        print(str(lis)+'\t', end='')  
    print('----------------------------------------------')
while(True):
    print("Seleccione: ")
    print("---------------------------")
    print("1.- moda")
    print("2.- media")
    print("3.- desviacion estandar")
    print("4.- summary")
    print("5.- Terminar")
    print("--------------------------")
    
    op=int(input())
    if op==1:
        moda()
    if op==2:
        media()
    if op==3:
        desvest()
    if op==4:
        moda()
        media()
        desvest()
    if op==5:
        break
