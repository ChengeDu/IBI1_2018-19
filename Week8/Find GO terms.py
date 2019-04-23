# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:49:25 2019

@author: Joanna
"""

import xml.dom.minidom
import pandas as pd
import re

def find(ID,result):
    for term in terms:
        parents=term.getElementsByTagName('is_a')
        geneid=term.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data==ID: 
                result.append(geneid) #means it is one of its child
                find(geneid,result)
        
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
defstrs=collection.getElementsByTagName("defstr")
terms=collection.getElementsByTagName("term")
IDs=[]
names=[]
definitions=[]
childnumber=[]
#these 4 lists are used to record id,name,definition & childnumber.
#result={}
for term in terms:
    defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
    if re.search('autophagosome',defstr)!=None: #judge whether it satisfies our need
        ID=term.getElementsByTagName('id')[0].childNodes[0].data
        name=term.getElementsByTagName('name')[0].childNodes[0].data
        IDs.append(ID)
        names.append(name)
        definitions.append(defstr)
        result=[] #for each ID, the childcodes number should start with 0
        find(ID,result)
        childnumber.append(len(result))
        #print(ID,' ',len(result))
        #parents=term.getElementsByTagName('is_a')
        #for parent in parents:
         #   child=parent.childNodes[0].data
          #  if child in result:
           #     result[child].add(ID)
            #else:
             #   result[child]={ID}


#print(childnumber)        
df=pd.DataFrame({'id':IDs,'name':names,'definition':definitions,'childnodes':childnumber})
# build a excel which has 4 parts

df.to_excel(r'C:\Users\Joanna\Desktop\黄帝内经\IBI1_2018-19\Week8\autophagosome.xlsx')