*** Settings ***
Variables  config/cfg.py
Library  pylib.WebOp

Suite Setup      openBrowser
Suite Teardown   closeBrowser

