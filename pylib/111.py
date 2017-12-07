# coding:utf8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('C://Git//IntelligentCorrection//report.html')
totalele = driver.find_element_by_xpath('//*[@id="total-stats"]/tbody/tr[1]/td[2]')
totalnum = int(totalele.text)
passele = driver.find_element_by_xpath('//*[@id="total-stats"]/tbody/tr[1]/td[3]')
passnum = int(passele.text)
percentage = format(round(passnum/float(totalnum),2),".2%")

detailContentele = driver.find_element_by_xpath('//table[@class="details"]')
detailContent = detailContentele.text

totalContentele = driver.find_element_by_id('total-stats')
totalContent = totalContentele.text

byTagContentele = driver.find_element_by_id('tag-stats')
byTagContent = byTagContentele.text

bySuiteContentele = driver.find_element_by_id('suite-stats')
bySuiteContent = bySuiteContentele.text



def createReportContent(detailContent, totalContent, byTagContent, bySuiteContent, percentage, reportSavePath):
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
    errornum = 98
    accessnum = 123122
    pernum = '0.02345%'
    total = 'errornum:%s，accessnum：%s，pernum：%s' % (errornum, accessnum, pernum)
    accesslist = u"<br><font size='4' style='font-weight:bold;'>请求概况：%s</font>" % total.decode('utf8')
    html = u"<html> <head><title></title><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head><body>" + accesslist + "<br>" + detailTable + "<font size='5' style='font-weight:bold;'>Test Statistics</font>" + totalTable + "<br>" + byTagTable + "<br>" + bySuiteTable + \
           u"<br><font size='4' style='font-weight:bold;'>更多详情请查看邮件附件【report.html】和【log.html】!!!</font></body></html>"
    read = open(reportSavePath, 'w')
    read.write(html.encode('utf8'))
    read.close
createReportContent(detailContent,totalContent,byTagContent,bySuiteContent,percentage,'C:\\Git\\IntelligentCorrection\\reportlog.html')

