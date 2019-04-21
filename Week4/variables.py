# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:35:45 2019

@author: Joanna
"""

a=178
b=178178
mod=b%7
c=b//7
if mod!=0:
    print('b cannot be divided by 7')
else:
    print('b can be divided by 7')
d=c//11
e=d//13
if a==e:
    print('a is same with b')
else:
    print('a is not same with b')

X=False
Y=False
#Z=X ^ Y
Z=(X and not Y) or (Y and not X)
print('Z=',Z)
W=(X!=Y)
print('W=',W)
if Z==W:
    print('Z is same to W')
else:
    print('Z is not same to W')

