# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:31 2019

@author: Joanna
"""

a=input('give me a string of words:')
a=a.split(' ')
listt=[]
for char in a:
    result=char[::-1]
    listt.append(result)
listt.sort()
listt.reverse()
print(listt)

