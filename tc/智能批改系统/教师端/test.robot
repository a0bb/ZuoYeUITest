*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.PrepareExercise
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
    bookmark