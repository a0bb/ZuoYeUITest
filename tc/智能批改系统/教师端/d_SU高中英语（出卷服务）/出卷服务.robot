*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.PrepareExercise
Library  pylib.Toolkit


*** Test Cases ***
流程-布置新作业_出卷服务
    VolumeServer   d_SU高中英语（出卷服务）  好好学习，天天向上
    ${volumeservertext}=    mygettext  //div[@class="item ng-scope"]/h4
    #log to console  ${volumeservertext}
    should be true  $volumeservertext==u'd_SU高中英语（出卷服务）'


流程-取消出卷
    CancelServer  d_SU高中英语（出卷服务）
    ${tohomepage}=   mygettext   //a[text()="回到首页"]
    should be true  $tohomepage==u'回到首页'