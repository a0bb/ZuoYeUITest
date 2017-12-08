*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.DealwithExam
Library  pylib.WebOpAdmin
Library  pylib.Toolkit
Library  pylib.WebOp

*** Test Cases ***
流程-后台发布成绩--0002
    LoginWebSiteAdmin
    sleep  10     # 后台有时不会及时刷新等待10s种
    ChooseTest    d_SU高中英语（模板出卷）
    TuPianYuChuLi
    TuPianYuXueSheng
    TuPianYuChengJi
    XueShengChengJi
    sleep  1
    ${compare}=  mygettext  //div[@class="toast-inner"]
    should be true  ${compare} == '发布成功'

流程-下载各个报告--0003
    ChangeHandle  智能批改
    DownloadFile  d_SU高中英语（模板出卷）      #d_SU高中英语（模板出卷）

流程-检查总分
    ${scores}=  GetGradeScore  d_SU高中英语（模板出卷）
    log to console  ${scores}
    ${compareScore}=  create list  111.7  141  82.5
    lists should be equal  ${scores}  ${compareScore}

