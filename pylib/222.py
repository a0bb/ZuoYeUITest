# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('C://Git//IntelligentCorrection//report.html','rb+'),"html5lib")
div = soup.find_all('div')[1]
print div
























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


