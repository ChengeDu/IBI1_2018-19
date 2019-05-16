# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:08:50 2019

@author: Joanna
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

I=1    #initial infected people
Ilist=[]
Ilist.append(I)

S=9999 #intial susceptible people
Slist=[]
Slist.append(S)

R=0    #initial recovered people
Rlist=[]
Rlist.append(R)

N=I+S+R  #population size
beta=0.3 #infect probability
gamma=0.05 #recover probability
time=[]
time.append(0)

for i in range(1000):
    Precover=gamma
    Pinfect=beta*Ilist[i]/N
    reI=[]
    inI=[]
    recovered=0
    infected=0
    reI=np.random.choice(range(2),Ilist[i],p=[Precover,1-Precover])
    #judge whether the infected people get recovered
    for j in reI:
        if j==0:
           recovered+=1 
    inI=np.random.choice(range(2),Slist[i],p=[Pinfect,1-Pinfect])
    #judge whether the susceptible people get infected
    for j in inI:
        if j==0:
           infected+=1 
    
    #add the number of people recovered in this time       
    Rlist.append(Rlist[i]+recovered) 
    #add the number of people infected and minus the number of people recovered
    #to get the infected number at this time
    Ilist.append(Ilist[i]+infected-recovered)
    #minus the number of people infected in this time    
    Slist.append(Slist[i]-infected)
    #record the time
    time.append(i+1) 
    
#plot the state of a person as time goes    
plt.plot(time,Ilist,label='infected')
plt.plot(time,Rlist,label='recovered')
plt.plot(time,Slist,label='susceptible')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()
#save this plot as png
#plt.savefig('C:/Users/Joanna/Desktop/黄帝内经/IBI1_2018-19/Week12/SIR.png')
    
    
    
