# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:27:44 2021

@author: Alexander Humberto Nina Pacajes
"""
import pandas as pd
import matplotlib.pyplot as plt
import random
df = pd.read_csv('voice.csv')
#bins para separarlo en quartiles o percentiles
#df['meanfreq'].plot(kind='hist')
#df['sd'].plot(kind='hist')
for col in df.columns:
    r = random.random()
    b = random.random()
    g = random.random()
    c = (r, g, b)
    plt.title(col)
    plt.hist(df[col],color=c)
    plt.show()
    plt.clf()
    plt.cla()


df.plot.bar(stacked=True)
#uno=df['meanfreq']
#dos=df['label']
#sns.set_theme(style="darkgrid")
#sns.countplot(x=uno,hue=dos)
#plt.show()