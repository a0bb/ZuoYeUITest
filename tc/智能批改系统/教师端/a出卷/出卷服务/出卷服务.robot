*** Settings ***
Library  Collections
Variables  cfg.py
Library  pylib.WebOpTeacher
Library  pylib.WebOpAdmin
Library  pylib.PrepareExercise.PrepareExercise
Library  pylib.Toolkit

*** Test Cases ***
流程-布置新作业_出卷服务 - tc1001
    VolumeServer   d_SU高中英语（出卷服务）_用例  好好学习，天天向上
    ${volumeservertext}=    mygettext  //div[@class="item ng-scope"]/h4/span
    log to console  ${volumeservertext}
    should be true  u"${volumeservertext}" == u"d_SU高中英语（出卷服务）_用例"

    [Teardown]  Run Keywords   CancelServer  d_SU高中英语（出卷服务）_用例
                ...  AND  ChangeHandle        管理后台
                ...  AND  DeleteAdminExcise   d_SU高中英语（出卷服务）_用例
                ...  AND  ChangeHandle        智能批改


流程-取消出卷 - tc1002
    VolumeServer   d_SU高中英语（出卷服务）  好好学习，天天向上
    CancelServer  d_SU高中英语（出卷服务）
    ${tohomepage}=   mygettext   //div[@class="m-v-30"]/span
    should be true  u"${tohomepage}" == u"本次制卷任务已取消"
    [Teardown]  Run Keywords  ChangeHandle        管理后台
                ...  AND  DeleteAdminExcise   d_SU高中英语（出卷服务）
                ...  AND  ChangeHandle        智能批改