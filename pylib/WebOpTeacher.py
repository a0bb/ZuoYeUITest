# coding:utf8

from selenium import webdriver
from config.cfg import *
from pylib.WebOp import WebOp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pylib import Toolkit
from selenium.webdriver.common.by import By
import subprocess
import os
import time


class WebOpTeacher():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # 用于调试的时候启动浏览器，没其他用处
    def setupWebTest(self):
        if WebOp.shared_wd:
            return

        WebOp.shared_wd = webdriver.Chrome()

        WebOp.shared_wd.implicitly_wait(1.5)

    # 登陆教师端
    def LoginWebSiteTeacher(self,username,password):
        WebOp.shared_wd.get(TeacherLoginUrl)
        WebOp.shared_wd.maximize_window()
        WebOp.shared_wd.find_element_by_css_selector('a[selenium="switch_type"]').click()  # 点击尚未绑定微信，使用用户名登录

        usernameele = WebOp.shared_wd.find_element_by_css_selector('input[selenium="username"]')  # 用户名
        usernameele.clear()
        usernameele.send_keys(username)

        passwordele = WebOp.shared_wd.find_element_by_css_selector('input[selenium="password"]')  # 密码
        passwordele.clear()
        passwordele.send_keys(password)

        WebOp.shared_wd.find_element_by_css_selector('button[selenium="submit"]').click()  # 登陆

        WebOp.shared_wd.find_element_by_css_selector('button[selenium="dismiss"]').click()  # 点击稍后再说
        time.sleep(1)
        WebOp.shared_wd.find_element_by_css_selector('button[selenium="dismiss"]').click()  # 点击我知道了

    # 登出教师端
    def OutWebSite(self):
        WebOp.shared_wd.find_elements_by_css_selector('.dropdown-toggle')[0].click()
        WebOp.shared_wd.find_elements_by_css_selector('a[selenium="logout"]')[0].click()

    # 切换 TAB页（首页、联考、试卷库等等）
    def EnterTab(self,name):
        try:
            tabLinkXpath = u"//*[text()='{}']".format(name)
            WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0].send_keys(Keys.ENTER)
            time.sleep(0.5)
        except:
            WebOp.shared_wd.find_elements_by_css_selector('.badge-fly')[0].click()
            time.sleep(0.5)

    # 根据作业的名称，查找对应的作业
    def FindHomeWork(self,homeWork):
        tabLinkXpath = u"//span[text()='{}']".format(homeWork)
        for no in range(9999):
            if Toolkit.IsElementPresentxpath(tabLinkXpath):
                break
            WebOp.shared_wd.find_element_by_css_selector('a[ng-click="selectPage(page + 1)"]').click()

    # 提交作业
    def SubmitHomeWork(self,homeWork):
        self.EnterTab(u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        self.FindHomeWork(homeWork)    # 先找到这个作业
        tabLinkXpath = u"//span[text()='{}']//../preceding-sibling::span/a[text()='请提交作业']".format(homeWork)
        homeWorkele = WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0]
        homeWorkele.click()

        WebOp.shared_wd.find_element_by_css_selector('.fa-cloud-upload').click()  # 提交作业
        WebOp.shared_wd.find_element_by_css_selector('.item-download').click()  # 点击“+可一次性添加多个班级作答试卷”
        cmd = ExternalPath + 'uploadPicture.exe' + " " + picturePath
        submitPicture = subprocess.Popen(cmd)
        submitPicture.wait()

        WebOp.shared_wd.find_element_by_css_selector('button[selenium="upload"]').click() # 添加完成，开始上传
        if not Toolkit.IsElementPresentxpath('//div[text()="上传确认"]'):
            WebOp.shared_wd.find_element_by_css_selector('button[selenium="upload"]').click()  # 添加完成，开始上传
        Toolkit.is_visible('//span[@class="ng-scope"]')
        WebOp.shared_wd.find_element_by_xpath('//span[@class="ng-scope"]').click()   # 确认无误，开始上传
        Toolkit.is_visible('//a[@selenium="finish"]')
        WebOp.shared_wd.find_element_by_xpath('//a[@selenium="finish"]').click()  # 我已传完
        time.sleep(2)

    # 在查看成绩中下载各种文件  还需完善
    def DownloadFile(self,homeWork):
        # 初始下目录
        currentTimeToD = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        createpath = downFilePath + currentTimeToD + '\\'
        Toolkit.mkdir(createpath)
        WebOp.shared_wd.refresh()
        self.EnterTab(u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        self.FindHomeWork(homeWork)
        tabLinkXpath = u"//span[text()='{}']//../preceding-sibling::span/a[text()='查看成绩']".format(homeWork)  # 点击查看成绩
        homeWorkele = WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0]
        homeWorkele.send_keys(Keys.ENTER)

        WebOp.shared_wd.find_elements_by_css_selector('div.ng-scope>div.clearfix>div.ng-scope')[2].click()  # 成绩单
        WebOp.shared_wd.find_elements_by_css_selector('div.pull-right>button')[0].click() # 点击下载年级成绩单
        cmd = ExternalPath + "downloadfile.exe" + " " + createpath + u'年级成绩单.xls'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        # time.sleep(2)

        WebOp.shared_wd.find_elements_by_css_selector('div.pull-right>button')[1].click()  # 点击下载各班成绩单
        Toolkit.is_visible('//span[text()=" 下载各班成绩单"]')     # 确定在“下载各班成绩单”的按钮出现（即弹出了下载框）执行下面步骤
        cmd = ExternalPath + "downloadfile.exe" + " " + createpath + u'各班成绩单（全年级成绩单）.zip'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(3)
        WebOp.shared_wd.find_element_by_css_selector(u'button[title="1401班"]').click() # 点击1401班
        WebOp.shared_wd.find_element_by_css_selector('div.pull-right>button').click()   # 点击下载班级成绩单
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'班级成绩单.xls'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(2)
        WebOp.shared_wd.find_element_by_css_selector(u'button[title="全年级"]').click() # 点击全年级
        WebOp.shared_wd.find_elements_by_css_selector('div.ng-scope>div.clearfix>div.ng-scope')[1].click()  # 试题分析
        WebOp.shared_wd.find_elements_by_css_selector('div.section-header>div.pull-right>button')[0].click()  # 下载年级试题分析表
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'年级试题分析表.xls'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(2)
        WebOp.shared_wd.find_elements_by_css_selector('div.section-header>div.pull-right>button')[1].click()  # 下载各班作答明细
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'各班作答明细（全年级成绩明细）.zip'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(5)
        WebOp.shared_wd.find_element_by_css_selector(u'button[title="1401班"]').click()  # 点击1401班
        WebOp.shared_wd.find_element_by_css_selector('div.pull-right>button').click()    # 下载班级作答明细
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'班级作答明细.xls'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(2)
        WebOp.shared_wd.find_elements_by_css_selector('div.ng-scope>div.clearfix>div.ng-scope')[3].click()  # 学生报告
        WebOp.shared_wd.find_element_by_css_selector('div.pull-left>button>span.ng-scope').click()   # 下载导出批阅报告
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'批阅报告.pdf'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        #time.sleep(2)
        WebOp.shared_wd.find_element_by_css_selector('div.slimScrollDiv div.student:nth-child(2)').click()  # 点击一个学生回到顶部
        hidden_submenu = WebOp.shared_wd.find_elements_by_css_selector('div.ng-scope>div.clearfix>div.ng-scope')[3]  # 学生报告
        ActionChains(WebOp.shared_wd).move_to_element(hidden_submenu).perform()
        #WebOp.shared_wd.find_elements_by_css_selector('div.ng-scope>div.clearfix>div.ng-scope')[3].click()  # 学生报告
        WebOp.shared_wd.find_element_by_xpath(u'//div[text()="导出报告"]').click()  # 导出报告
        #dcbgele.send_keys(Keys.ENTER)
        WebOp.shared_wd.find_element_by_css_selector('div.section-body>button').click()  # 下载生成班级批阅报告
        Toolkit.is_visible('//span[text()=" 生成班级批阅报告"]')  # 确定在“生成班级批阅报告”的按钮出现（即弹出了下载框）执行下面步骤
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'全部批阅报告.pdf'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        # time.sleep(5)
        WebOp.shared_wd.find_element_by_css_selector('div.pull-right-sm>button').click() # 下载导出统计报告
        Toolkit.is_visible('//span[text()=" 导出统计报告"]')  # 确定在“导出统计报告”的按钮出现（即弹出了下载框）执行下面步骤
        cmd = ExternalPath + 'downloadfile.exe' + " " + createpath + u'统计报告.pdf'
        pp = subprocess.Popen(cmd.encode('gb2312'))
        pp.wait()
        time.sleep(5)

    # 获取全年级的平均分、最高分、最低分
    def GetGradeScore(self,homeWork):
        self.EnterTab(u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        WebOp.shared_wd.refresh()
        self.FindHomeWork(homeWork)  # 先找到这个作业
        tabLinkXpath = u"//span[text()='{}']//../preceding-sibling::span/a[text()='查看成绩']".format(homeWork)
        homeWorkele = WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0]
        homeWorkele.click()
        # 获取平均分
        aveScorele = WebOp.shared_wd.find_element_by_css_selector('div.block-success>span:nth-child(2)')
        aveScore = aveScorele.text
        # 获取最高分
        maxScorele = WebOp.shared_wd.find_element_by_css_selector('div.block-success>span:nth-child(6)')
        maxScore = maxScorele.text
        # 获取最低分
        minScorele = WebOp.shared_wd.find_element_by_css_selector('div.block-success>span:nth-child(10)')
        minScore = minScorele.text
        return [aveScore,maxScore,minScore]






# **************调试部分*******************
def test():
    webop = WebOp()
    webop.openBrowser()
    wo = WebOpTeacher()
    wo.setupWebTest()
    wo.LoginWebSiteTeacher('wangshihua1', 'wangshihua1')
    Toolkit.MyClickElement(u'//span[text()="d_SU高中英语（模板出卷）"]//../preceding-sibling::span/a[text()="查看成绩"]')
    #wo.SubmitHomeWork(u'd_SU高中英语（模板出卷）')
    #wo.Template(u'd_SU高中英语（模板出卷）')
    # wo.Self_help(u"d_SU高中英语（出卷服务）",u" 好好学习，天天向上")
    # wo.CancelServer(u'd_SU高中英语（出卷服务）')
    #wo.DeleteExcise(u'测试题干串题')
    #wo.Template(u'd_SU高中英语（模板出卷）')
    #wo.findHomeWork(u'高考模拟测验_自动阅卷')
    #Toolkit.ChangeHandle(u'智能批改')
    #wo.DownloadFile(u'd_SU高中英语（模板出卷）')
    #print wo.GetGradeScore(u"d_SU高中英语（模板出卷）")



if __name__ == '__main__':
    test()