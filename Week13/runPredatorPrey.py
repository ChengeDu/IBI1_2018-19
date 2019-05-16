# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:13:19 2019

@author: Joanna
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom
import random


def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    #cpsFile = open("predator-prey.cps","w")
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()

def getcsv():
    xml_to_cps()
    os.system('CopasiSE.exe predator-prey.cps')    


def plot():
    global predator
    global prey
    recording=open('modelResults.csv','r')
    count=0
    results=[[],[],[]]

    for line in recording:
        line=line.rstrip()
        count+=1
    #use split to devide the line into 3 parts
        if count!=1:
            lineinfo=line.split(',') 
            results[0].append(lineinfo[0])
            results[1].append(lineinfo[1])
            results[2].append(lineinfo[2])
       

    results=np.array(results)
    results=results.astype(np.float)

    plt.plot(results[0],results[1],label=predator)
    plt.plot(results[0],results[2],label=prey)

    plt.xlabel('time')
    plt.ylabel('population size')
    plt.title('Time course')
    plt.legend()
    plt.show()

    plt.plot(results[1],results[2])
    plt.xlabel('predator population')
    plt.ylabel('prey population')
    plt.title('Limit cycle')
    #plt.legend()
    plt.show()

def changeparameter():
    global para
    DOMTree=xml.dom.minidom.parse("predator-prey.xml")
    collection=DOMTree.documentElement
    parameters=collection.getElementsByTagName("parameter")

    for parameter in parameters:
        print(parameter.getAttribute('name'))
        #set random number to the 'value'
        parameter.setAttribute('value',random.random())
        #record the changed 'value' in a list 'para'
        para.append(parameter.getAttribute('value'))
        print(parameter.getAttribute('value'))
        
        

#-----------------------Running a Copasi model from within Python--------------    
os.chdir('C:/Users/Joanna/Desktop/黄帝内经/IBI1_2018-19/Week13')
predator='Predator (b=0.02,d=0.4)'
prey='Prey (b=0.1,d=0.02)'
getcsv()


#-----------------------Reading and plotting simulation results----------------
plot() #a fucntion for reading and plotting



#------------Changing values and running the simulation again------------------
para=[] #to record the new parameters
changeparameter() #read xml and change its 4 parameters

#However, using setAttribute will not change the information in the original file,
#so next reserve the 4 changed parameters in the new predator-prey.xml file. (this
#step doesn't have corresponding code in this program so the following figure doesn't
#change)

#operate the function xml_to_cps() again to renew the predator-prey.cps
xml_to_cps()
#use os.system('CopasiSE.exe predator-prey.cps') to renew the modelResults.csv
os.system('CopasiSE.exe predator-prey.cps')
#use the same way to get an array just as get the 'results' above

#set the label for the figure
predator='Predator (b='+str(para[0])+',d='+str(para[1])+')'
prey='Prey (b='+str(para[2])+',d='+str(para[3])+')'
plot()



#--------------------------Running many simulations----------------------------
#since the simulation time is 100, plot made my computer broke down, so just hid the following
#codes for security
'''
for i in range(100):
    para=[]
    #change the 4 parameters of predator-prey.xml
    changeparameter()
    #reserve the 4 changed parameters in the new predator-prey.xml file (this
    #step doesn't have corresponding code in this program so the following figures 
    #doesn't change)
    xml_to_cps()
    os.system('CopasiSE.exe predator-prey.cps')
    #set the label for the figure
    predator='Predator (b='+str(para[0])+',d='+str(para[1])+')'
    prey='Prey (b='+str(para[2])+',d='+str(para[3])+')'
    #plot the figure each time
    plot()  
'''
    