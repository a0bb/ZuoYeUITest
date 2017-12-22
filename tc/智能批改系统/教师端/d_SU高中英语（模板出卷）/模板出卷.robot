*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.PrepareExercise
Library  pylib.Toolkit


*** Test Cases ***
流程-布置新作业_模板出卷 - tc1003
    Template   d_SU高中英语（模板出卷）2   # 模板出卷 名称为“d_SU高中英语（模板出卷）”
    ${compare}=   mygettext  //a[text()="阅卷管理"]
    should be true  ${compare} == '阅卷管理'

流程-删除练习 - tc1004
    DeleteExcise   d_SU高中英语（模板出卷）2