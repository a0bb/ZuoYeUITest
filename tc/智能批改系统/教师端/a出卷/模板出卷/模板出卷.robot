*** Settings ***
Library  Collections
Variables  config/cfg.py
Library  pylib.WebOpTeacher
Library  pylib.PrepareExercise
Library  pylib.WebOpAdmin
Library  pylib.Toolkit


*** Test Cases ***
流程-布置新作业_模板出卷 - tc1003
    Template   d_SU高中英语（模板出卷）_用例   # 模板出卷 名称为“d_SU高中英语（模板出卷）”
    ${compare}=   mygettext  //a[text()="阅卷管理"]
    should be true  u"${compare}" == u"阅卷管理"
    entertab  首页
    [Teardown]  run keywords  deleteexcise  d_SU高中英语（模板出卷）_用例   请提交作业
                ...      AND  ChangeHandle        管理后台
                ...      AND  DeleteAdminExcise   d_SU高中英语（模板出卷）_用例
                ...      AND  ChangeHandle        智能批改


