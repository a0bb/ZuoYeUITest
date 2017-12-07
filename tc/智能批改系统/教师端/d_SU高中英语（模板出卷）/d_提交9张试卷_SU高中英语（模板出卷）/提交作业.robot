*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher

*** Test Cases ***
提交作业 -- 0001
    SubmitHomeWork  d_SU高中英语（模板出卷）      # 提交作业
