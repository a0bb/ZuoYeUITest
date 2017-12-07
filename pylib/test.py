# coding:utf8

# def createReportContent(detailContent, totalContent, byTagContent, bySuiteContent, percentage, reportSavePath):
#     result = detailContent.split("\n")
#     sDetail = ''
#     for index in range(len(result)):
#         if (index != len(result)):
#             sDetail = sDetail + result[index] + "<br>"
#         else:
#             sDetail = sDetail + result[index]
#     detailTable = "<font size='5' style='font-weight:bold'>Summary Information</font><br><table width='1000' border='1' cellpadding='1' cellspacing='1'><tr><td width='100%'>" + 'Run Pass Rate: ' + percentage + "</td></tr><tr><td width='100%'>" + sDetail + "</td></tr></table>"
#
#     totalTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%''>Total Statistics</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
#     result = totalContent.split("\n")
#     del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     for index in range(len(result)):
#         if ((index + 1) % 2 == 1):
#             totalTable = totalTable + "<tr><td>" + result[index] + "</td>"
#         else:
#             s = result[index]
#             items = s.split(" ")
#             for item in items:
#                 totalTable = totalTable + "<td>" + item + "</td>"
#             sColor = "";
#             if (items[2] == "0"):
#                 sColor = "green"
#             else:
#                 sColor = "red"
#             totalTable = totalTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
#                 1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
#                              2] + "</font></center></td></tr>"
#     totalTable = totalTable + "</table>"
#     byTagTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%'>Statistics by Tag</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
#     result = byTagContent.split("\n")
#     del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     for index in range(len(result)):
#         if ((index + 1) % 2 == 1):
#             byTagTable = byTagTable + "<tr><td>" + result[index] + "</td>"
#         else:
#             s = result[index]
#             items = s.split(" ")
#             for item in items:
#                 byTagTable = byTagTable + "<td>" + item + "</td>"
#             sColor = "";
#             if (items[2] == "0"):
#                 sColor = "green"
#             else:
#                 sColor = "red"
#             byTagTable = byTagTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
#                 1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
#                              2] + "</font></center></td></tr>"
#     byTagTable = byTagTable + "</table>"
#     bySuiteTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%'>Statistics by Suite</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
#     result = bySuiteContent.split("\n")
#     del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     # del result[0]
#     for index in range(len(result)):
#         if ((index + 1) % 2 == 1):
#             bySuiteTable = bySuiteTable + "<tr><td>" + result[index] + "</td>"
#         else:
#             s = result[index]
#             items = s.split(" ")
#             for item in items:
#                 bySuiteTable = bySuiteTable + "<td>" + item + "</td>"
#             sColor = "";
#             if (items[2] == "0"):
#                 sColor = "green"
#             else:
#                 sColor = "red"
#             bySuiteTable = bySuiteTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
#                 1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
#                                2] + "</font></center></td></tr>"
#     bySuiteTable = bySuiteTable + "</table>"
#     html = "<html> <head><title></title><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head><body>" + detailTable + "<font size='5' style='font-weight:bold;'>Test Statistics</font>" + totalTable + "<br>" + byTagTable + "<br>" + bySuiteTable + "<br><font size='5' style='font-weight:bold;'>更多详情请查看邮件附件【report.html】和【log.html】!!!</font></body></html>"
#     print html
#     read = open(reportSavePath, 'w')
#     read.write(html)
#     read.close
# createReportContent('//table[@class="details"]','total-stats','tag-stats','suit-stats','format(round(${pass}/float(${total}),2),".2%")','C:\\Git\\IntelligentCorrection\\reportlog.html')






import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_mail(open_file, attfile1, attfile2):
    # 如果是list请以逗号分隔
    mailto_list = ['425548772@qq.com','wangshihua@hexin.im']
    mail_host = "smtp.163.com"
    mail_user = "18366105118@163.com"
    mail_pass = "wsh18366105118"

    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    detailTime = time.strftime('%H:%M:%S',time.localtime(time.time()))

    send_header = u"[自动化测试报告]- ".encode("utf-8") + today +" "+detailTime
    me=u"启明合心".encode("utf8")
    msg = MIMEMultipart()
    msg['Subject'] = send_header
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)

    fp = open(open_file,"r")
    content = fp.read()
    msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
    fp.close()

    #log report
    att1 = MIMEText(open(attfile1, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    #result report
    att2 = MIMEText(open(attfile2, 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="log.html"'
    msg.attach(att2)

    try:
        server = smtplib.SMTP_SSL()
        server.connect(mail_host,994)
        server.login(mail_user,mail_pass)
        server.sendmail(mail_user, mailto_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    if send_mail(r'C:/Git/ZuoYeUITest/reportlog.html', r'C:/Git/ZuoYeUITest/report.html', r'C:/Git/ZuoYeUITest/log.html'):
        print u"发送成功"
    else:
        print u"发送失败"