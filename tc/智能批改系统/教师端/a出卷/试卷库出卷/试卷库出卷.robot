*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.Toolkit
Library  pylib.WebOpAdmin
Library  pylib.PrepareExercise


*** Test Cases ***
流程-提交作业 - tc1005
    bookmark   高考模拟测验_正常流程       # 试卷库出卷
    SubmitHomeWork   高考模拟测验_正常流程      # 提交作业
    ${compare}=   mygettext   //span[text()="正在努力批改中"]
    should be true  u"${compare}" == u"正在努力批改中"
    [Teardown]  run keywords  deleteexcise  高考模拟测验_正常流程  作业批改中
                ...      AND  ChangeHandle        管理后台
                ...      AND  DeleteAdminExcise   高考模拟测验_正常流程
                ...      AND  ChangeHandle        智能批改


流程-删除练习 - tc1004
    bookmark   高考模拟测验_正常流程
    DeleteExcise   高考模拟测验_正常流程  请提交作业
    [Teardown]  run keywords  ChangeHandle        管理后台
                ...      AND  DeleteAdminExcise   高考模拟测验_正常流程
                ...      AND  ChangeHandle        智能批改


