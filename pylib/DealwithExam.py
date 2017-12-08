# coding:utf8

from selenium import webdriver
from cfg import *
from pylib.WebOp import WebOp
from pylib import Toolkit
from pylib.WebOpAdmin import WebOpAdmin
from pylib.WebOpTeacher import WebOpTeacher
import time


class DealwithExam():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 对考试列表中的“d_SU高中英语（模板出卷）”在任务面板进行处理（9张试卷）
    def ChooseTest(self,exciseName):
        WebOp.shared_wd.find_element_by_css_selector(u'span[title="考试列表"]').click() # 选择考试列表
        WebOp.shared_wd.find_elements_by_link_text(exciseName)[0].click()  # 选择考试“d_SU高中英语（模板出卷）”
        WebOp.shared_wd.find_element_by_css_selector('div.btn-group>a.border').click()  # 点击任务面板

    # 第1步--图片预处理
    def TuPianYuChuLi(self):
        if not Toolkit.IsElementPresentcss('tr[auth="paper_anchor||is_super"]>td>a.btn-success'):    # 判断第1步 图片预处理 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="paper_anchor||paper_indexing||is_super"]').click()
        WebOp.shared_wd.find_element_by_css_selector('tr[auth="paper_anchor||is_super"]>td>a.btn-success').click()  # 定位点--处理按钮
        if Toolkit.IsElementPresentxpath(u"//div[text()='没有数据']"):
            WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()
        else:
            pass  # 过后补充这种情况

    # 第2A步--图片与学生
    def TuPianYuXueSheng(self):
        if not Toolkit.IsElementPresentcss('tr[auth="paper_bind||is_super"]>td>a.btn-success'):    # 判断第2A步 图片与学生 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="paper_bind||paper_grouping||is_super"]').click()
        WebOp.shared_wd.find_element_by_css_selector('tr[auth="paper_bind||is_super"]>td>a.btn-success').click()  # 学生关联--处理按钮
        if Toolkit.IsElementPresentxpath(u"//div[text()='没有数据']"):
            WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
        else:
            WebOp.shared_wd.find_element_by_css_selector('div>button.btn-white').click()    # 需要完善

    # 第2B步--图片与成绩
    def TuPianYuChengJi(self):
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="marking_choice||is_super"]'):      # 判断选择题是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="marking_choice||is_super"]>td>a.btn-success').click()
            if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
            else:
                pass  # 过后补充这种情况

        # 填空题
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="marking_blanks||blank_score||blank_tag||is_super"]'):      # 判断填空题是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="marking_blanks||blank_score||blank_tag||is_super"]>td>a.btn-success').click()
            if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
            else:
                for Cnum in range(99):
                    if not Toolkit.IsElementPresentxpath('//tr//td[position()=4 and text()!="0"]'):
                        break
                    biaozhuEles = WebOp.shared_wd.find_elements_by_xpath(u'//a[text()="标注"]')
                    for biaozhuele in biaozhuEles:
                        biaozhuele.click()
                        if Toolkit.IsElementPresentcss('div.text-center>button.btn-primary'):  # 判断进入***题这个按钮是否存在
                            WebOp.shared_wd.find_element_by_css_selector('div.text-center>button.btn-primary').click()
                        if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                            WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
                            break
                        for num in range(99):
                            WebOp.shared_wd.find_element_by_css_selector('button[ng-click="selectAll()"]').click()  # 全选
                            WebOp.shared_wd.find_element_by_css_selector('button[ng-click="submit()"]').click()  # 提交
                            if Toolkit.IsElementPresentcss('div.text-center>button.btn-primary'):  # 判断进入**题这个按钮是否存在
                                WebOp.shared_wd.find_element_by_css_selector('div.text-center>button.btn-primary').click()  # 点击进入**题
                                time.sleep(1)
                            if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                                WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
                                break
                        break


                WebOp.shared_wd.find_elements_by_css_selector('.text-left')[0].click()   # 全选考试题
                WebOp.shared_wd.find_element_by_css_selector('div.bg-grey>button').click()    # 点击一建打分
                time.sleep(1.5)    # 不能显示等待因为元素之前是存在的
                WebOp.shared_wd.find_element_by_xpath('//div[@class="pull-right"]//button').click()    # 点击返回

        # 改错题
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="marking_correction||is_super"]'):  # 判断改错题是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="marking_correction||is_super"]>td>a.btn-success').click()
            if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
            else:
                for Cnum in range(99):   # 题目数量
                    if not Toolkit.IsElementPresentxpath(u'//tr//td[position()=6 and text()!="0"]'):    # 判断下有没有
                        break
                    biaozhuEles = WebOp.shared_wd.find_elements_by_xpath(u'//tr//td[position()=6 and text()!="0"]/following-sibling::td//a//span[text()="标注"]')
                    for biaozhuele in biaozhuEles:
                        biaozhuele.click()
                        WebOp.shared_wd.find_elements_by_xpath(u'//div[text()="过滤: "]//button')[1].click()  # 获取所有的 过滤出来的答案
                        for num in range(99):
                            WebOp.shared_wd.find_element_by_css_selector('button[ng-click="selectAll()"]').click()  # 全选
                            WebOp.shared_wd.find_element_by_css_selector('i.fa-check').click()  # 点击对号（这里判断不出到底对错，就都选对了）
                            if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
                                WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
                                break
                        break
                WebOp.shared_wd.find_element_by_css_selector('div.pull-right>button').click()   # 点击返回
                time.sleep(1)

        # 作文题
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="marking_writing||is_super"]'):  # 判断作文题是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="marking_writing||is_super"]>td>a.btn-success').click()
            WebOp.shared_wd.find_element_by_css_selector('div.pull-right>button').click()    # 返回

        # 打分框
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="marking_scores||is_super"]'):  # 判断打分框是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="marking_scores||is_super"]>td>a.btn-success').click()
        if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
            WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回

        # 试卷打分
        if not Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]>td.text-center>a'):   # 判断第2B步 图片与成绩 是不是展开的
            WebOp.shared_wd.find_element_by_css_selector('div[auth="marking_choice||marking_blanks||blank_score||blank_tag||marking_correction||marking_writing||marking_scores||paper_score||is_super"]').click()
        if Toolkit.IsElementPresentcss('tr[auth="paper_score||is_super"]'):  # 判断试卷打分是否存在
            WebOp.shared_wd.find_element_by_css_selector('tr[auth="paper_score||is_super"]>td>a.btn-success').click()
        if Toolkit.IsElementPresentxpath(u'//div[text()="本题已处理完成！"]'):
            WebOp.shared_wd.find_element_by_css_selector('button.btn-default').click()  # 点击返回
        else:
            WebOp.shared_wd.find_element_by_css_selector('button>span').click()   # 点击 保存，下一个
            WebOp.shared_wd.find_element_by_css_selector('div>button.btn-white').click()    # 点击返回

    # 第3步--学生与成绩
    def XueShengChengJi(self):
        WebOp.shared_wd.find_element_by_css_selector('div>button[auth="publish||is_super"]').click()
        Toolkit.Prompt()
        WebOp.shared_wd.find_element_by_css_selector('div>button.btn-white').click()



def test():
    wo = WebOpAdmin()
    wo.openBrowser()
    pr = WebOpTeacher()
    pr.LoginWebSiteTeacher('0001yangyang', '0001yangyang')
    wo.LoginWebSiteAdmin()
    de = DealwithExam()
    de.ChooseTest(u'高考模拟测验')
    # de.TuPianYuChuLi()
    # de.TuPianYuXueSheng()
    # de.TuPianYuChengJi()
    de.XueShengChengJi()

if __name__ == '__main__':
        test()

