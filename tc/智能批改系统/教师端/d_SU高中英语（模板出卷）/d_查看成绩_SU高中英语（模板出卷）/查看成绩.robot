*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.DealwithExam
Library  pylib.WebOpAdmin
Library  pylib.Toolkit
Library  pylib.WebOp

*** Test Cases ***
后台发布成绩--0002
    LoginWebSiteAdmin
    sleep  10    # 后台有时不会及时刷新
    ChooseTest    d_SU高中英语（模板出卷）
    TuPianYuChuLi
    TuPianYuXueSheng
    TuPianYuChengJi
    XueShengChengJi
    sleep  1



下载各个报告--0003
    ChangeHandle  智能批改
    DownloadFile  d_SU高中英语（模板出卷）      #d_SU高中英语（模板出卷）