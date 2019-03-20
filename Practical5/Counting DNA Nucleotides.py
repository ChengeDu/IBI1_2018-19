# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:13:02 2019

@author: Joanna
"""
import matplotlib.pyplot as plt

labels='A','T','C','G'
a=input('give me a sequence of DNA:')
DNA={}
for char in a:
    if char in DNA:
       DNA[char]+=1
    else:
       DNA[char]=1
print(str(DNA))
length=len(a)
#sizeA="%.2f%%" % (DNA['A']/length*100)
#sizeT="%.2f%%" % (DNA['T']/length*100)
#sizeC="%.2f%%" % (DNA['C']/length*100)
#sizeG="%.2f%%" % (DNA['G']/length*100)
sizes=[DNA['A'],DNA['T'],DNA['C'],DNA['G']]
explode=(0.025,0.05,0.1,0.15)
colors='lightgreen','gold','lightskyblue','lightcoral'
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False)
plt.axis('equal')
plt.show()
