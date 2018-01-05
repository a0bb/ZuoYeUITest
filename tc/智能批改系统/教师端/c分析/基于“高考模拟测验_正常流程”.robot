*** Keywords ***
suite setup action
    bookmark   高考模拟测验_正常流程            # 试卷库出卷
    SubmitHomeWork   高考模拟测验_正常流程      # 提交作业
    changehandle  管理后台
    ChooseTest    高考模拟测验_正常流程
    TuPianYuChuLi
    TuPianYuXueSheng
    DealwithUnNo   高考模拟测验_正常流程   # 教师处理那一个未关联的学生
    # 图片与成绩下的题目处理
    XuanZeTi
    TianKongTi
    GaiCuoTi
    # ZuoWenTi 作文题不需要标注
    DaFenKuang
    ShiJuanDaFen
    # 图片与成绩下的题目处理
    XueShengChengJi
    sleep  1

*** Settings ***
Library  Collections
Variables  config/cfg.py
Library  pylib.WebOpTeacher
Library  pylib.Toolkit
Library  pylib.WebOpAdmin
Library  pylib.PrepareExercise
Library  pylib.WebOp
Library  pylib.DealwithExam.PictureAndGrade
Library  pylib.DealwithExam.DealwithExam

Suite Setup  suite setup action
Suite Teardown  run keywords  deleteexcise  高考模拟测验_正常流程  查看成绩
                ...      AND  ChangeHandle        管理后台
                ...      AND  DeleteAdminExcise   高考模拟测验_正常流程
                ...      AND  ChangeHandle        智能批改


*** Test Cases ***
流程-下载各个报告 - tc1006
    ChangeHandle  智能批改
    DownloadFile  高考模拟测验_正常流程      #d_SU高中英语（模板出卷）


流程-检查总分 - tc1007
    ChangeHandle  智能批改
    ${scores}=  GetGradeScore  高考模拟测验_正常流程
    log to console  ${scores}
    ${compareScore}=  create list  92.9  141  10
    lists should be equal  ${scores}  ${compareScore}