*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.DealwithExam
Library  pylib.DealwithExam.PictureAndGrade
Library  pylib.WebOpAdmin
Library  pylib.Toolkit
Library  pylib.WebOp

*** Test Cases ***
流程-后台发布成绩 - tc2001   # 需绑定tc1005
    changehandle  管理后台
#    sleep  10     # 后台有时不会及时刷新等待10s种
    ${paperNum}=  evaluate  12
    ChooseTest    d_SU高中英语（模板出卷）   ${paperNum}
    TuPianYuChuLi
    TuPianYuXueSheng
    DealwithUnNo   d_SU高中英语（模板出卷）   # 教师处理那一个未关联的学生
    # 图片与成绩下的题目处理
    XuanZeTi
    TianKongTi
    GaiCuoTi
    ZuoWenTi
    DaFenKuang
    ShiJuanDaFen
    # 图片与成绩下的题目处理
    XueShengChengJi
    sleep  1
    ${compare}=  mygettext  //div[@class="toast-inner"]
    should be true  ${compare} == '发布成功'

流程-下载各个报告 - tc1006
    ChangeHandle  智能批改
    DownloadFile  d_SU高中英语（模板出卷）      #d_SU高中英语（模板出卷）

流程-检查总分 - tc1007
    ${scores}=  GetGradeScore  d_SU高中英语（模板出卷）
    log to console  ${scores}
    ${compareScore}=  create list  111.7  141  82.5
    lists should be equal  ${scores}  ${compareScore}

