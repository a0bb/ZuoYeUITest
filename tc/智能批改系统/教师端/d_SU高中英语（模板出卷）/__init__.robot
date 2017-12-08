*** Keywords ***

*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.PrepareExercise
Library  pylib.DealwithExam
Library  pylib.WebOpAdmin
Library  pylib.Toolkit
Library  pylib.WebOp



Suite Setup     Template   d_SU高中英语（模板出卷）   # 模板出卷 名称为“d_SU高中英语（模板出卷）”
Suite Teardown  Run Keywords  DeleteExcise   d_SU高中英语（模板出卷）
                ...  AND  DeleteExcise   d_SU高中英语（模板出卷）2
                ...  AND  LoginWebSiteAdmin
                ...  AND  DeleteAdminExcise   d_SU高中英语（模板出卷）
                ...  AND  DeleteAdminExcise   d_SU高中英语（出卷服务）
                ...  AND  DeleteAdminExcise   d_SU高中英语（模板出卷）2