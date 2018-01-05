# coding:utf8
import paramiko
import time
import config.cfg as cfg
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Result():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 获取 error.log的当前这一天日志数量
    def GetErrorNum(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('106.14.161.218', '22', 'root', 'sigmaLOVE2017')
            conTimeerror = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 格式： 2017/11/14
            cmderror = 'cd /mnt/logs/nginx/;grep -c' + " " + conTimeerror + " " + 'error.log'
            stdin, stdout, stderr = ssh.exec_command(cmderror)
            errornum = int(stdout.read())
            return errornum
            # print stdout.read()+stderr.read()
            ssh.close()
        except:
            return stderr.read()

    # 获取 access.log的当前这一天的日志数量
    def GetAccessNum(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('106.14.161.218', '22', 'root', 'sigmaLOVE2017')
            conTimeaccess = time.strftime("%d/%b/%Y", time.localtime())  # 04/Dec/2017
            cmdaccess = 'cd /mnt/logs/nginx/;grep -c' + " " + conTimeaccess + " " + 'access.log'
            stdin, stdout, stderr = ssh.exec_command(cmdaccess)
            accessnum = int(stdout.read())
            return accessnum
            # print stdout.read()+stderr.read()
            ssh.close()
        except:
            return stderr.read()

    # 获取 error/access 百分比(重复访问造成性能降低)
    # def GetPer(self):
    #     errorNum = float(self.GetErrorNum())
    #     accessNum = float(self.GetAccessNum())
    #     per = errorNum / accessNum
    #     return "%.6f%%" % (per * 100)

    # 生成文件并放到linux
    def OutTxt(self):
        errornum = self.GetErrorNum()
        accessnum = self.GetAccessNum()
        per = "%.6f%%" % ((float(errornum)/float(accessnum)) * 100)
        perExam = "%.2f%%" % ((float(cfg.errorExam)/float(cfg.totalExam)) * 100)
        total = u'请求概况  出错请求数量：%s，总请求数量：%s，出错请求占比：%s' %(errornum,accessnum,per)
        totalExam = u'后端群反馈问题概况  反馈问题对应考试数量：%s，发布的考试的数量：%s，有问题考试占比：%s' %(cfg.errorExam,cfg.totalExam,perExam)
        if int(cfg.errorExam) == 0:
            totalExam = u'今天没有反馈问题，棒棒的！'
        htmltotal = "<br><font size='4' style='font-weight:bold;'>" + total +  "</font>" + "<br><font size='4' style='font-weight:bold;'>" + totalExam +  "</font>"
        with open('./Statistics.txt','w') as outfile:
            outfile.write(htmltotal.encode('utf8'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('106.14.161.218', '22', 'root', 'sigmaLOVE2017')
        sftp = ssh.open_sftp()
        sftp.put('./Statistics.txt','/mnt/logs/Statistics.txt')
        shell = 'scp /mnt/logs/Statistics.txt root@192.168.0.5:/usr/local/hexin/qareport'
        ssh.exec_command(shell)

    # report.log 重新生成
    def createReportContent(self,detailContent, totalContent, byTagContent, bySuiteContent, percentage, reportSavePath):
        result = detailContent.split("\n")
        sDetail = ''
        for index in range(len(result)):
            if (index != len(result)):
                sDetail = sDetail + result[index] + "<br>"
            else:
                sDetail = sDetail + result[index]
        detailTable = "<font size='5' style='font-weight:bold'>Summary Information</font><br><table width='1000' border='1' cellpadding='1' cellspacing='1'><tr><td width='100%'>" + 'Run Pass Rate: ' + percentage + "</td></tr><tr><td width='100%'>" + sDetail + "</td></tr></table>"

        totalTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%''>Total Statistics</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
        result = totalContent.split("\n")
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        for index in range(len(result)):
            if ((index + 1) % 2 == 1):
                totalTable = totalTable + "<tr><td>" + result[index] + "</td>"
            else:
                s = result[index]
                items = s.split(" ")
                for item in items:
                    totalTable = totalTable + "<td>" + item + "</td>"
                sColor = "";
                if (items[2] == "0"):
                    sColor = "green"
                else:
                    sColor = "red"
                totalTable = totalTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
                    1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
                                 2] + "</font></center></td></tr>"
        totalTable = totalTable + "</table>"
        byTagTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%'>Statistics by Tag</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
        result = byTagContent.split("\n")
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        for index in range(len(result)):
            if ((index + 1) % 2 == 1):
                byTagTable = byTagTable + "<tr><td>" + result[index] + "</td>"
            else:
                s = result[index]
                items = s.split(" ")
                for item in items:
                    byTagTable = byTagTable + "<td>" + item + "</td>"
                sColor = "";
                if (items[2] == "0"):
                    sColor = "green"
                else:
                    sColor = "red"
                byTagTable = byTagTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
                    1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
                                 2] + "</font></center></td></tr>"
        byTagTable = byTagTable + "</table>"
        bySuiteTable = "<table width='1000' border='1' cellpadding='1' cellspacing='1'><tr bgcolor='#DCDCDC'><td width='40%'>Statistics by Suite</td><td>Total</td><td>Pass</td><td>Fail</td><td>Elapsed</td><td>Pass/Fail</td></tr>"
        result = bySuiteContent.split("\n")
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        del result[0]
        for index in range(len(result)):
            if ((index + 1) % 2 == 1):
                bySuiteTable = bySuiteTable + "<tr><td>" + result[index] + "</td>"
            else:
                s = result[index]
                items = s.split(" ")
                for item in items:
                    bySuiteTable = bySuiteTable + "<td>" + item + "</td>"
                sColor = "";
                if (items[2] == "0"):
                    sColor = "green"
                else:
                    sColor = "red"
                bySuiteTable = bySuiteTable + "<td><center><font style='font-weight:bold;color:green'>" + items[
                    1] + "/</font><font style='font-weight:bold;color:" + sColor + "'>" + items[
                                   2] + "</font></center></td></tr>"
        bySuiteTable = bySuiteTable + "</table>"
        errornum = self.GetErrorNum()
        accessnum = self.GetAccessNum()
        pernum = self.GetPer()
        total = 'errornum:%s，accessnum：%s，pernum：%s' % (errornum, accessnum, pernum)
        accesslist = u"<br><font size='4' style='font-weight:bold;'>请求概况：%s</font>" % total.decode('utf8')
        html = u"<html> <head><title></title><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head><body>" + accesslist + "<br>" + detailTable + "<font size='5' style='font-weight:bold;'>Test Statistics</font>" + totalTable + "<br>" + byTagTable + "<br>" + bySuiteTable + \
               u"<br><font size='4' style='font-weight:bold;'>更多详情请查看邮件附件【report.html】和【log.html】!!!</font></body></html>"
        read = open(reportSavePath, 'w')
        read.write(html.encode('utf8'))
        read.close

    # 发送邮件
    def send_mail(self,open_file, attfile1, attfile2):
        # 如果是list请以逗号分隔
        receivers = ['425548772@qq.com','wangshihua@hexin.im']
        mail_host = "smtp.163.com"
        sender = "18366105118@163.com"
        mail_pass = "sigmalove2017"

        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        detailTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        send_header = u"[自动化测试报告]- ".encode("utf-8")+ today +" "+detailTime
        me = u"启明合心".encode("utf8")
        msg = MIMEMultipart()
        msg['Subject'] = Header(send_header,'utf8')      # 主题
        msg['From'] = Header(me, 'utf8')                  # 发自哪儿
        msg['To'] = Header(";".join(receivers)) # 发给谁

        fp = open(open_file, "r")
        content = fp.read()
        msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
        fp.close()

        # log report
        att1 = MIMEText(open(attfile1, 'rb').read(), 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(att1)

        # result report
        att2 = MIMEText(open(attfile2, 'rb').read(), 'base64', 'gb2312')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="log.html"'
        msg.attach(att2)

        try:
            server = smtplib.SMTP_SSL()
            server.connect(mail_host,465)
            server.login(sender, mail_pass)
            server.sendmail(sender, receivers, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False



# **************调试部分*******************
def test():
    res = Result()
    # if res.send_mail(r'C:/Git/ZuoYeUITest/reportlog.html', r'C:/Git/ZuoYeUITest/report.html', r'C:/Git/ZuoYeUITest/log.html'):
    #     print u"发送成功"
    # else:
    #     print u"发送失败"
    res.OutTxt()



if __name__ == '__main__':
    test()


























