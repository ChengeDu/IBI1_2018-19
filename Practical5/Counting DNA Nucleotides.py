# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:13:02 2019

@author: Joanna
"""

a=input('give me a sequence of DNA:')
DNA={}
for char in a:
    if char in ['A','T','C','G']:
       if char in DNA:
          DNA[char]+=1
       else:
          DNA[char]=1
print(str(DNA))
#DNA
#print(DNA)
import matplotlib.pyplot as plt
#labels='A','T','C','G'
#sizes=[DNA['A'],DNA['T'],DNA['C'],DNA['G']]
labels=DNA.keys()
sizes=DNA.values()
#explode=(0.025,0.05,0.1,0.15)
#colors='lightgreen','gold','lightskyblue','lightcoral'
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False)
plt.axis('equal')
plt.show()

#if the letters we imput are less than 4 types, then the original codes 'explode' will get an error