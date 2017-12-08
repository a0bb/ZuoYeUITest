*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.Toolkit

*** Test Cases ***
流程-提交作业 -- 0001
    SubmitHomeWork  d_SU高中英语（模板出卷）      # 提交作业
    ${compare}=   mygettext   //span[text()="正在努力批改中"]
    should be true  ${compare} == '正在努力批改中'

