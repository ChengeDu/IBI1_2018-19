# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:11:31 2019

@author: Joanna
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:08:39 2019

@author: Joanna
"""
#coding:utf-8
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender='3180111437@zju.edu.cn'
#receiver='1666148325@qq.com'
# SMTP service
mail_host="smtp.zju.edu.cn"  #server
mail_user="3180111437"    #user
mail_pass="xxxxx"   #password

#print the sender information
print('From:',sender)
print('Password:',mail_pass)

xaddress=open('address_information.csv','r')
con=open('body.txt','r')
content=con.read()
for line in xaddress:
    line=line.rstrip()
    #use split to devide the line into 3 parts
    lineinfo=line.split(',')    
    name=lineinfo[0]
    receiver=lineinfo[1]
    subject=lineinfo[2]

    #if it is line 1, then skip the following procedure
    if name=='name':
        continue
    #bo is used for record whether it is a correct address
    bo=False
    
    #judge whether it is a valid address
    if re.search(r'[^,]+@[0-9a-zA-Z]+.com',receiver):
        #actually .com is not enough to check
        bo=True
        print(receiver,end='')
        print(': Correct Address!')
    elif re.search(r'[^,]+@[0-9a-zA-Z]+.[a-zA-Z]+.cn',receiver):
        bo=True
        print(receiver,end='')
        print(': Correct Address!')
    else:
        print(receiver,end='')
        print(': Wrong Address!')

    #if it is a correct address, then send emails:
    if bo==True:
       message=content.replace('User',name)
       msg=MIMEText(message,'plain','utf-8')
       msg['From']=Header('Joanna','utf-8')
       msg['To']=Header(receiver,'ascii')
       msg['Subject']=Header(subject,'utf-8')        
       try:
           server=smtplib.SMTP(mail_host,25)
           server.connect(mail_host,25)
           server.login(mail_user,mail_pass)
           server.sendmail(sender,receiver,msg.as_string())
           server.quit()
           print('Mail sent successfully!')
       except smtplib.SMTPException:
           print('Mail sent failed!')

        