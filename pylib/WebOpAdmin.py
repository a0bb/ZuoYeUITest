# coding:utf8

from cfg import *
from pylib.WebOp import WebOp
from selenium.webdriver.common.action_chains import ActionChains
from pylib import Toolkit
import time
from pylib.WebOpTeacher import WebOpTeacher


class WebOpAdmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 新开窗口并切换到的后台登陆
    def LoginWebSiteAdmin(self):
        jsonNewWindow = 'window.open("{}")'.format(AdminLoginJsonUrl)
        WebOp.shared_wd.execute_script(jsonNewWindow)
        time.sleep(2)
        Toolkit.ChangeHandle('perpetua')
        WebOp.shared_wd.close()
        Toolkit.ChangeHandle(u'智能批改')
        adminNewWindow = 'window.open("{}")'.format(AdminLoginUrl)
        WebOp.shared_wd.execute_script(adminNewWindow)
        Toolkit.ChangeHandle(u'管理后台')
        WebOp.shared_wd.find_element_by_id('logo').click()
        time.sleep(2)

    # 删除后台考试列表中的考试
    def DeleteAdminExcise(self,exciseName):
        WebOp.shared_wd.find_element_by_css_selector(u'span[title="考试列表"]').click()  # 选择考试列表
        Toolkit.is_visible('//span[text()="考试名称"]')
        WebOp.shared_wd.find_elements_by_css_selector('table.channel-table td')[0].click()  # 点击全部
        xpath = u'//a[text()="{}"]//..//following-sibling::td//a//span[text()="删除"]'.format(exciseName)
        if Toolkit.IsElementPresentxpath(xpath):
            WebOp.shared_wd.find_elements_by_xpath(xpath)[0].click()  # 选择考试“d_SU高中英语（模板出卷）”并删除第一个
            Toolkit.Prompt()







# ***************调试*********************
def test():
    pass
    wo = WebOpAdmin()
    wo.openBrowser()
    pr = WebOpTeacher()
    pr.LoginWebSiteTeacher('0001yangyang', '0001yangyang')
    wo.LoginWebSiteAdmin()
    wo.DeleteAdminExcise(u'd_SU高中英语（模板出卷）')
    wo.DeleteAdminExcise(u'd_SU高中英语（出卷服务）')
    # wo.dealwithExam(u'高考模拟测验')

if __name__ == '__main__':
        test()