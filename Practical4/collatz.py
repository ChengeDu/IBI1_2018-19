# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:05:09 2019

@author: Joanna
"""

n=37
print(n)
#repeat until n=1
while n!=1:
#if n is even then n/2 else 3*n+1
    if n%2==0:
        n=n/2
    else:
        n=3*n+1
    print(n)