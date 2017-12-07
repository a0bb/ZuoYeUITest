*** Settings ***
Library    Collections
Variables  cfg.py
Library    pylib.WebOpTeacher

Suite Setup    LoginWebSiteTeacher  &{TeacherUser}[name]  &{TeacherUser}[pw]


Suite Teardown

