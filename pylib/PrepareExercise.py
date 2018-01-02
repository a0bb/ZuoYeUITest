# coding:utf8

from cfg import *
from pylib import Toolkit
from pylib.WebOp import WebOp
from pylib.WebOpTeacher import WebOpTeacher
from selenium.webdriver.common.keys import Keys
import subprocess
import time


class PrepareExercise:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 布置新作业--出卷服务
    def VolumeServer(self, exerciseName, leaveMassage):
        WebOpTeacher.EnterTab(WebOpTeacher(), u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        newTest = WebOp.shared_wd.find_element_by_css_selector('button[selenium="create_exercise_btn"]')  # 布置作业
        newTest.send_keys(Keys.ENTER)  # 元素被DIV覆盖，click改成ENTER

        WebOp.shared_wd.find_element_by_class_name('ui-select-match-text').click()
        # print WebOp.shared_wd.find_elements_by_class_name('ui-select-choices-row-inner')[2].text #打印一下选中的什么学科
        WebOp.shared_wd.find_elements_by_class_name('ui-select-choices-row-inner')[2].click()  # 选高中英语
        WebOp.shared_wd.find_element_by_xpath(u'//div[text()="出卷服务"]').click()   # 选择出卷服务
        WebOp.shared_wd.find_element_by_css_selector('button[selenium="submit"]').click()  # 开始布置
        exciseNameele = WebOp.shared_wd.find_element_by_id('name')
        exciseNameele.clear()
        exciseNameele.send_keys(exerciseName)  # 练习名称

        WebOp.shared_wd.find_element_by_css_selector('label[for="radio_type_0"]').click()  # 答题卡样式
        WebOp.shared_wd.find_element_by_css_selector('label[for="radio_size_0"]').click()  # 答题卡板式

        # 上传
        WebOp.shared_wd.find_element_by_css_selector('span[ng-if="!$loading"]').click()  # 添加文档
        # os.system(ExternalPath + 'uploadfile.exe')  # 调用AutoIt上传
        cmd = ExternalPath + 'uploadfile.exe' + " " + filePath
        volumeServerFile = subprocess.Popen(cmd.encode('gb2312'))
        volumeServerFile.wait()
        leaveMassageele = WebOp.shared_wd.find_element_by_css_selector('textarea[ng-model="exercise.message"]')  # 留言
        leaveMassageele.clear()
        leaveMassageele.send_keys(leaveMassage)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click="confirm()"]').click()  # 提交
        WebOp.shared_wd.find_element_by_css_selector('button[ng-click="$close()"]').click()  # 确认无误，提交
        Toolkit.is_visible('//h4[@class="title pull-left-xs"]')

    # 出卷服务--取消制卷
    def CancelServer(self, homeWork):
        WebOpTeacher.EnterTab(WebOpTeacher(), u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        WebOpTeacher.FindHomeWork(WebOpTeacher(),homeWork)
        tabLinkXpath = u"//span[text()='{}']//../preceding-sibling::span/a[text()='制卷中...']".format(homeWork)  # 这个要取消出卷的试卷名称
        homeWorkele = WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0]
        homeWorkele.click()
        WebOp.shared_wd.find_element_by_css_selector('a>span.ng-scope').click()  # 取消制卷
        numEle = WebOp.shared_wd.find_element_by_css_selector('div>label')
        num = numEle.text[-2:]
        inputEle = WebOp.shared_wd.find_element_by_css_selector('div.labels>input')
        inputEle.send_keys(num)
        WebOp.shared_wd.find_element_by_css_selector('div>button.btn-danger').click()  # # 我已了解，继续

    # 布置新作业--模板出卷
    def Template(self, exerciseName):
        WebOpTeacher.EnterTab(WebOpTeacher(),u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        newTest = WebOp.shared_wd.find_element_by_css_selector('button[selenium="create_exercise_btn"]')  # 布置作业
        newTest.send_keys(Keys.ENTER)  # 元素被DIV覆盖，click改成ENTER
        WebOp.shared_wd.find_element_by_class_name('ui-select-match-text').click()
        WebOp.shared_wd.find_elements_by_class_name('ui-select-choices-row-inner')[2].click()  # 选高中英语
        time.sleep(1)
        WebOp.shared_wd.find_element_by_css_selector('div[selenium-value="00000011"]').click()  # 选择模板！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        WebOp.shared_wd.find_element_by_css_selector('button[selenium="submit"]').click()  # 开始布置

        exerciseNameele = WebOp.shared_wd.find_element_by_id('name')
        exerciseNameele.clear()
        exerciseNameele.send_keys(exerciseName)

        WebOp.shared_wd.find_element_by_css_selector('.controls>.btn-tiny').click()  # 添加文档
        # os.system(ExternalPath + 'upload.exe')  # 调AUTOIT
        cmd = ExternalPath + 'uploadfile.exe' + " " + filePath
        volumeServerFile = subprocess.Popen(cmd.encode('gb2312'))
        volumeServerFile.wait()
        num = Toolkit.GetAnswer(answerPath, 7)
        tingliele = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[0]  # 听力题
        tingliele.clear()
        tingliele.send_keys(num[0])

        yuedulijiele = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[1]  # 阅读理解
        yuedulijiele.clear()
        yuedulijiele.send_keys(num[1])

        wanxingtiankong = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[2]  # 完型填空
        wanxingtiankong.clear()
        wanxingtiankong.send_keys(num[2])

        duanwentiankong = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[3]  # 短文填空
        duanwentiankong.clear()
        duanwentiankong.send_keys(num[3])

        duanwengaicuo = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[4]  # 短文改错
        duanwengaicuo.clear()
        duanwengaicuo.send_keys(num[4])
        WebOp.shared_wd.find_element_by_css_selector('button[ng-click="viewCorrection()"]').click()  # 点击“确认，开始标记答案”

        zuowenbiaoti = WebOp.shared_wd.find_element_by_css_selector('.question-content>.form-group>.controls>input')  # 作文标题
        zuowenbiaoti.clear()
        zuowenbiaoti.send_keys(num[5])

        zuowenneirong = WebOp.shared_wd.find_elements_by_css_selector('div>textarea')[5]  # 作文内容
        zuowenneirong.clear()
        zuowenneirong.send_keys(num[6])

        WebOp.shared_wd.find_element_by_css_selector('button[selenium="submit"]').click()  # 提交
        Toolkit.is_visible('//button[@selenium="share_btn"]')

    # 布置新作业，自助出卷  ToDo
    def Self_help(self):
        WebOpTeacher.EnterTab(WebOpTeacher(), u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        newTest = WebOp.shared_wd.find_element_by_css_selector('button[selenium="create_exercise_btn"]')  # 布置作业
        newTest.send_keys(Keys.ENTER)  # 元素被DIV覆盖，click改成ENTER
        WebOp.shared_wd.find_element_by_class_name('ui-select-match-text').click()
        WebOp.shared_wd.find_elements_by_class_name('ui-select-choices-row-inner')[2].click()  # 选高中英语
        time.sleep(1)
        WebOp.shared_wd.find_element_by_xpath('//div[text()="自助出卷"]').click()  # 选自助出卷
        exciseNamele = WebOp.shared_wd.find_element_by_css_selector('div>input.ng-touched')  # 试卷名称
        exciseNamele.clear()
        exciseNamele.send_keys(u'd_SU高中英语（自助出卷）')

        WebOp.shared_wd.find_element_by_css_selector('button[selenium="submit"]').click()  # 开始布置

    # 布置新作业--试卷库出卷
    def BookMark(self,exerciseName):
        WebOpTeacher.EnterTab(WebOpTeacher(), u'试卷库')
        WebOp.shared_wd.find_element_by_xpath('//div[text()="【SU】ScriptUser"]').click()
        xpath = u'//span[text()="{}"]'.format(exerciseName)
        WebOp.shared_wd.find_element_by_xpath(xpath).click()
        Toolkit.is_visible('//button/span')
        WebOp.shared_wd.find_element_by_css_selector('button.btn-success').click()     # 点击使用本试卷
        Toolkit.is_visible('//div/a[@class="active"]')


    # 删除练习（在作业批改中这个阶段的）
    def DeleteExcise(self, homeWork,homeworkStatus):
        # homework:作业名称
        # homeworkStatus:作业状态（自助制卷中...|请提交作业|作业批改中|查看成绩）
        WebOpTeacher.EnterTab(WebOpTeacher(), u'首页')
        Toolkit.is_visible('//i[@class="fa fa-pencil"]')  # 确定已经切换到首页了
        tabLinkXpath = u"//span[text()='{}']//../preceding-sibling::span/a[text()='{}']".format(homeWork,homeworkStatus)  # 要删除练习的试卷名称（找在作业批改中的）
        WebOpTeacher.FindHomeWork(WebOpTeacher(), homeWork)
        homeWorkele = WebOp.shared_wd.find_elements_by_xpath(tabLinkXpath)[0]
        homeWorkele.click()
        WebOp.shared_wd.find_element_by_link_text('作业布置').click()  # 作业布置
        WebOp.shared_wd.find_elements_by_css_selector('span.caret')[0].click()  # 编辑练习下拉框
        WebOp.shared_wd.find_element_by_css_selector('a>span.ng-scope').click()  # 删除练习
        numEle = WebOp.shared_wd.find_element_by_css_selector('div.modal-content div>label')
        num = numEle.text[-2:]
        inputEle = WebOp.shared_wd.find_element_by_css_selector('div.labels>input')
        inputEle.send_keys(num)
        WebOp.shared_wd.find_element_by_css_selector('div>button.btn-danger').click()  # 我已了解，继续


# **************调试部分*******************
def test():
    wo = WebOpTeacher()
    wo.setupWebTest()
    wo.LoginWebSiteTeacher('0001yangyang', '0001yangyang')
    pe = PrepareExercise()

    #wo.SubmitHomeWork(u'd_SU高中英语（模板出卷）')
    pe.Template(u'd_SU高中英语（模板出卷）')
    #pe.VolumeServer(u"d_SU高中英语（出卷服务）",u" 好好学习，天天向上")
    # wo.CancelServer(u'd_SU高中英语（出卷服务）')
    #wo.DeleteExcise(u'测试题干串题')
    #wo.findHomeWork(u'高考模拟测验_自动阅卷')
    #wo.DownloadFile(u'高中语文作文')



if __name__ == '__main__':
    test()