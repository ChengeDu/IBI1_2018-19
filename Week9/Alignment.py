# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:39:53 2019

@author: Joanna
"""

#import numpy
def allignment(seq1,seq2,name1,name2):
    leng=min([len(seq1),len(seq2)]) #just need to compare the shorter length of two sequences
    #print(len(seq1),' ',len(seq2))
    value=0
    score=0 #to record the blosum score
    totalsame=0
    align='' #align is a string to record the alignment sequence
    for i in range(leng):
        location1=-1 # -1 means the initial setting of location
        location2=-1
        for j in range(len(s)):
            if s[j]==seq1[i]:
                location1=j+1
            if s[j]==seq2[i]:
                location2=j+1
            #record the blosum value location of seq1[i]&seq2[i]in the blosum list
            if location1!=-1 and location2!=-1: # these two locations have found
                break
        value=int(blosum[location1][location2]) #get the score for this base pair
        score=score+value
        if seq1[i]==seq2[i]:
            totalsame+=1
            align=align+seq1[i]
        else:
            if value>=0:
                align=align+'+'
            else:
                align=align+' '
    
    #print in the following codes
    print(name1)
    print(seq1)

    print('Alignment')
    print(align)

    print(name2)
    print(seq2)
    
    rescore=score/leng #normalised the total score
    print('total score ',score)
    print('normalised score ',rescore)
    
    percentage=totalsame/leng
    totaldiff=leng-totalsame
    print('edit_distance ',totaldiff)
    print('identicalpercentage ','%.2f%%' % (percentage*100))

#I write the results into a txt file in the following codes
'''    
    results=open('Results.txt','a')
    results.write('\n'+name1)
    results.write('\n'+seq1)
    results.write('\n'+'Alignment')
    results.write('\n'+align)
    results.write('\n'+name2)
    results.write('\n'+seq2)
    results.write('\n'+'total score:   '+str(score))
    results.write('\n'+'normalised score:   '+str(rescore))
    results.write('\n'+'edit_distance:   '+str(totaldiff))
    results.write('\n'+'identicalpercentage:   '+str('%.2f%%' % (percentage*100)))
    results.write('\n')
'''

#there are 3 files called Seq1,Seq2,Seq3
#file1 is human gene
file1=open('Seq1.txt') 
count=0
for line in file1:
    count+=1
    if count==2:
        name1=line[1:len(line)-1] #reserve the name
    if count==3:
        seq1=line #reserve the human gene sequence(there is only one line for the gene in my Seq1.txt file)

#file2 is mouse gene        
file2=open('Seq2.txt')
count=0
for line in file2:
    count+=1
    if count==2:
        name2=line[1:len(line)-1]
    if count==3:
        seq2=line

#file3 is random gene        
file3=open('Seq3.txt')
count=0
for line in file3:
    count+=1
    if count==2:
        name3=line[1:len(line)-1]
    if count==3:
        seq3=line
        
file4=open('BLOSUM62.txt')
blosum=[]
count=0
s='' #a string to record the amino aicd order in the above and the left of the blosum62
for line in file4:
    count+=1
    if count==1:
        for i in range(len(line)):
            if line[i]!=' ':
                s=s+line[i] #reserve the amino acid order
    ll=line.split()
    blosum.append(ll) #use list reserve the blosum62
    
allignment(seq1,seq2,name1,name2)
allignment(seq1,seq3,name1,name3)
allignment(seq2,seq3,name2,name3)