# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
mailto_list=['425548772@qq.com']           #收件人(列表)
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="18366105118@163.com"                           #用户名
mail_pass="sigmalove2017"                             #密码
mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com
def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
for i in range(1):                             #发送1封，上面的列表是几个人，这个就填几
    if send_mail(mailto_list,"电话","电话是XXX"):  #邮件主题和邮件内容
        #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print "done!"
    else:
        print "failed!"







# sender = '18366105118@163.com'
# receiver = 'wangshihua@hexin.im'
# subject = 'python'
# smtpserver = 'smtp.163.com'
# username = '18366105118@163.com'
# password = 'sigmalove2017'
#
# msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
#
# msg['Subject'] = subject
# msg['From'] = '123'
#
# smtp = smtplib.SMTP_SSL(smtpserver,994)
# # smtp.connect('smtp.qq.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()


