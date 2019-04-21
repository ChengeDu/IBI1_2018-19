# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:22:27 2019

@author: Joanna
"""

a=input()
n=int(a)
print(n,' is ',end="")
#another way: a=a+' is '
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
    # another way:   if n!=0:
    #                   a=a+'2**'+str(count-1)+'+'
    #                else:
    #                   a=a+'2**'+str(count-1)
    