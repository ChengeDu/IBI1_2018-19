import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender='3180111437@zju.edu.cn'
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
    receiveadd=lineinfo[1]
    subject=lineinfo[2]

    #if it is line 1, then skip the following procedure
    if name=='name':
        continue
    #bo is used for record whether it is a correct address
    bo=False
    
    #judge whether it is a valid address
    re_email=re.compile(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')
    if re_email.match(receiveadd):
        bo=True
        print(receiveadd,': Correct Address!')
    else:
        print(receiveadd,': Wrong Address!')

    #if it is a correct address, then send emails:
    if bo==True:
       #modify the content of User
       message=content.replace('User',name)
       msg=MIMEText(message,'plain','utf-8')
       
       sendname='Joanna'
       sendinfo=Header(sendname,'utf-8')
       sendinfo.append(sender,'ascii')
       msg['From']=sendinfo
       
       receiveinfo=Header(name,'utf-8')
       receiveinfo.append(receiveadd,'ascii')
       msg['To']=receiveinfo
       
       msg['Subject']=Header(subject,'utf-8')        
       try:
           server=smtplib.SMTP(mail_host,25)
           server.connect(mail_host,25)
           server.login(mail_user,mail_pass)
           server.sendmail(sender,receiveadd,msg.as_string())
           server.quit()
           print('Mail sent successfully!')
       except smtplib.SMTPException:
           print('Mail sent failed!')

#close the file
xaddress.close()
con.close()        