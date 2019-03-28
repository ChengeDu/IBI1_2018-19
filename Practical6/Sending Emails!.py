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
# 第三方 SMTP 服务
mail_host="smtp.zju.edu.cn"  #设置服务器
mail_user="3180111437"    #用户名
mail_pass="xxxxx"   #口令 

#xaddress=open('abcd.txt','r')
xaddress=open('address_information.csv','r')
con=open('body.txt','r')
content=con.read()
for line in xaddress:
    line=line.rstrip()
    name=str(re.findall(r'^([a-zA-Z]+)',line))
    leng=len(name)-2
    name=name[2:leng]
    #at first I forget that [::]cannot change the original 'name' sequence 
    subject=str(re.findall(r'To.+',line))
    leng1=len(subject)-2
    subject=subject[2:leng1]
    print(name,' ',end='')
    if name=='name':
        continue
    bo=False
    if re.search(r'[^,]+@[0-9a-zA-Z]+.com',line):
        #actually .com is not enough to check
        receiver=re.findall(r'[^,]+@[0-9a-zA-Z]+.com',line)
        print(receiver)
        bo=True
        print('Correct Address!')
    elif re.search(r'[^,]+@[0-9a-zA-Z]+.[a-zA-Z]+.cn',line):
        receiver=re.findall(r'[^,]+@[0-9a-zA-Z]+.[a-zA-Z]+.cn',line)
        print(receiver)
        bo=True
        print('Correct Address!')
    else:
        print('Wrong Address!')
    #a better way: re_mail=re.compile(r^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')
    #              re_loginname=re.compile(r'(\S+)@')
    
    if bo==True:
       message=content.replace('User',name)
       msg=MIMEText(message,'plain','utf-8')
       msg['From']=Header('Joanna','utf-8')
       msg['To']=Header('practical','utf-8')
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

        
#a better solution from my classmates:
#use .split to divide a line from address_information.csv to 3 line
#that means: ['Mary']
#            ['ibidiletest2@163.com']
#            ['To:...']
#it is easy to find the 3 things I want          
