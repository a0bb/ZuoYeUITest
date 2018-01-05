*** Settings ***
Library    Collections
Variables  config/cfg.py
Library    pylib.WebOpTeacher
Library    pylib.WebOpAdmin
Library    pylib.Toolkit

Suite Setup   Run Keywords  LoginWebSiteTeacher  &{TeacherUser}[name]  &{TeacherUser}[pw]
              ...      AND  LoginWebSiteAdmin
              ...      AND  ChangeHandle        智能批改


Suite Teardown

