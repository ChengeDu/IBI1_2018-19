# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:31:20 2019

@author: Joanna
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:08:50 2019

@author: Joanna
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

time=[]
for i in range(1001):
    time.append(i)

for i in range(10):
    N=10000  #total number of the whole population
    # record initial infected people
    Ilist=[]
    Ilist.append(1)
    
    # intial vaccinated people
    V=N*i*10//100

    #record initial recovered people
    Rlist=[]
    Rlist.append(0)
    
    # record intial susceptible people
    Slist=[]
    # 1 is the initial infected number, 0 is initial recovered number
    Slist.append(N-1-V-0) 
    
    beta=0.3
    gamma=0.05
    
    for j in range(1000):
        Precover=gamma #recover probability
        Pinfect=beta*Ilist[j]/N #infect probability
        reI=[] #record whether infected is recovered 
        inI=[] #record whether susceptible people is infected 
        recovered=0
        infected=0
        reI=np.random.choice(range(2),Ilist[j],p=[Precover,1-Precover])
        #judge whether the infected people get recovered
        for k in reI:
            if k==0:
               recovered+=1 
        inI=np.random.choice(range(2),Slist[j],p=[Pinfect,1-Pinfect])
        #judge whether the susceptible people get infected
        for k in inI:
            if k==0:
               infected+=1 
        
        #add the number of people recovered in this time       
        Rlist.append(Rlist[j]+recovered)
        #add the number of people infected and minus the number of people recovered
        #to get the infected number at this time
        Ilist.append(Ilist[j]+infected-recovered)
        #minus the number of people infected in this time
        Slist.append(Slist[j]-infected)
    
    if i!=0:
        percentage=str(i*10)+'%'  #percentage shows the vaccination rate  
    else:
        percentage=str(0)
    plt.plot(time,Ilist,label=percentage)

Ilist=[]
#since all people get vaccinated, the infected number should be 0
for i in range(1001):
    Ilist.append(0)        
plt.plot(time,Ilist,label='100%')   

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()
#save this plot as png
#plt.savefig('C:/Users/Joanna/Desktop/黄帝内经/IBI1_2018-19/Week12/SIR_vaccination.png')
    
    
    
