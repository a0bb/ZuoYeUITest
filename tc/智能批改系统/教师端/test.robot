*** Settings ***
Library  pylib.PrepareExercise
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.DealwithExam
Library  pylib.WebOpAdmin
Library  pylib.Toolkit
Library  pylib.WebOp

*** Test Cases ***
流程-登陆 - login
    LoginWebSiteTeacher  &{TeacherUser}[name]  &{TeacherUser}[pw]
    LoginWebSiteAdmin
    ChangeHandle        智能批改

流程-后台发布成绩 - test
    changehandle  管理后台
    sleep  10     # 后台有时不会及时刷新等待10s种
    ChooseTest    d_SU高中英语（模板出卷）  12
    TuPianYuChuLi
    TuPianYuXueSheng
    DealwithUnNo    # 教师处理那一个未关联的学生
    TuPianYuChengJi
    XueShengChengJi
    sleep  1
    ${compare}=  mygettext  //div[@class="toast-inner"]
    should be true  ${compare} == '发布成功'