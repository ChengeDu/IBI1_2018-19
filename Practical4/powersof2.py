# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:22:27 2019

@author: Joanna
"""

n=1750
print(n,'=',end="")
if n==0:
    print('0')
while n!=0:
    m=1
    count =0
    #find the largest 2^n which is smaller than n
    while n>=m:
          m=m*2
          count=count+1
    m=m//2
    n=n-m
    #n-the largest 2^n
    if n!=0:
        print('2**',count-1,'+',end="")
    else:
        print('2**',count-1)
    