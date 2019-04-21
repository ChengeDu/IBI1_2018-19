# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:17:52 2019

@author: Joanna
"""
import re
import fractions

def intext():
    global l
    for i in range(len(ss)):
        k=int(ss[i])
        if k<1 or k>23:
            return(False)
        l.append(k)
    return(True)

def calcu(i,a,b):
        if i==0:
           return(a+b)
        elif i==1:
           return(a-b)
        elif i==2:
           return(b-a)
        elif i==3:
           return(a*b)
        elif i==4 and (b!=0):
           return(fractions.Fraction(a,b))
          #if a % b==0:
          #   return(a//b)
        elif i==5 and (a!=0):
           return(fractions.Fraction(b,a))
           #if b % a==0:
           #   return(b//a)
        return(-1)

def point24(ll):
    global flag
    global count
    leng=len(ll)
    if flag:
        return(-1) #means already found,so do not need to continue the following sentence,just
                   #return back to the former recursion
    if leng==1:
       if ll[0]==24:
            print('Yes')
            #qwq=True
            return(-1) #-1 means I find the solution
       return(-2)
    if not flag:          
       #print(qwq)
       for i in range(leng-1):
           count+=1
           for j in range(i+1,leng):
               count+=1
               for k in range(6):
                   count+=1
                   a=ll[i]
                   b=ll[j]
                   m=calcu(k,a,b)
                   if m!=-1:
                       ll.remove(a)
                       ll.remove(b)
                       ll.append(m)
                       #print('ll',ll)
                       if (point24(ll)==-1) and (not flag):
                           flag=True
                           #print('Find out')
                           print('Recursion times:',count)
                           #break
                       ll.remove(m)
                       ll.append(a)
                       ll.append(b)
               #if qwq:
                    #break
           #if qwq:
              #break
#Actually I want to return to the main program when the answer is found, however,
# I found using 'exit' is not good because I cannot see the results. So finally I
# chose flag to decrease the operation times of calculate and judgment statements,
# but I still wonder if there is a better solution.                            
                              
    

s=input('Please input numbers to computer 24:(use ‘,’ to divide them)')
ss=re.split(r',',s) 
l=[]
flag=False
count=0
if intext():
    #can use tuples to return 2 variables
    point24(l)
    if not flag:
        print('No')
        print('Recursion times:',count)
#change the names and make them more meaningful
#output in the same section
