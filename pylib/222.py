# coding=utf8

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://zuoye.hexin.im')

sleep(10)
print driver.title