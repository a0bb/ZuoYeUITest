*** Settings ***
Library  Selenium2Library
Library  pylib.Result
Variables  cfg.py


*** Test Cases ***
发送邮件 - result002
    sleep  10
    ${reportpath}=   set variable   C://Git//ZuoYeUITest//report.html
    ${logpath}=      set variable   C://Git//ZuoYeUITest//log.html
    ${reportlogpath}=   set variable  C://Git//ZuoYeUITest//reportlog.html
    open browser   ${reportpath}  chrome
    sleep  3
    ${detailContent}=   get text  Xpath=//table[@class="details"]
    ${totalContent}=    get text  id=total-stats
    ${byTagContent}=    get text  id=tag-stats
    ${bySuiteContent}=  get text  id=suite-stats
    ${total}=           get text  Xpath=//*[@id="total-stats"]/tbody/tr[1]/td[2]
    ${pass}=            get text  Xpath=//*[@id="total-stats"]/tbody/tr[1]/td[3]
    ${persenttag}=      evaluate  format(round(${pass}/float(${total}),2),'.2%')

    createReportContent  ${detailContent}  ${totalContent}  ${byTagContent}  ${bySuiteContent}  ${persenttag}  ${reportlogpath}
    close browser
    send mail  ${reportlogpath}   ${reportpath}  ${logpath}
    log to console  邮件发送成功
