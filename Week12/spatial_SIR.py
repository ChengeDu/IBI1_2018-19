# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:10:22 2019

@author: Joanna
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptiable population which was different from the guidance
#since judging 8 neighbours around the person who is in the corner of the 
#figure is troublesome. Therefore, I added a border around the population
population=np.zeros((102,102))
for i in range(102):
    #to seperate it from the person, I used '-1' for tagging.
    population[0,i]=-1 
    population[101,i]=-1
    population[i,0]=-1
    population[i,101]=-1

#0 for susceptible people, 1 for infected, 2 for recovered
outbreak = np.random.choice(range(1,101),2)
x=outbreak[0]
y=outbreak[1]
population[x,y]=1
infected=[]
infected.append([x,y])

print('time= 0') #print the initial situation
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

beta=0.3 #infect probability
gamma=0.05 #recover probability

for i in range(1,101):
    renewinfected=[]
    leng=len(infected)
    for j in range(leng):
        x=infected[j][0]
        y=infected[j][1]
        
        #judge the 8 neighbour
        for j in range(-1,2):
               for k in range(-1,2):
                   #rule out the person himself
                   if j!=0 and k!=0:
                     #judge whether the neighbour is susceptible
                      if population[x+j,y+k]==0:
                         neighbour=np.random.choice(range(2),1,p=[beta,1-beta])
                         #judge whether the neighbour get infected
                         if neighbour==0:
                            renewinfected.append([x+j,y+k])
                            population[x+j,y+k]=1
        person=np.random.choice(range(2),1,p=[gamma,1-gamma])
        #judge whether the person get recovered
        if person==0:
            population[x,y]=2
        else:
            #the person isn't recovered, then add the location to next infected loop
            renewinfected.append([x,y]) 
    infected=[]
    #renew the infected people information
    infected=renewinfected.copy()
    if i==10 or i==50 or i==100:
        print('time=',i)
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    
                     
                            
       