*** Settings ***
Library  Selenium2Library
Library  pylib.Result
Variables  cfg.py


*** Test Cases ***
生成请求概况
    # 把生成的请求概述的文件放到linux相应的目录下
    OutTxt