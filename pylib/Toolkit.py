# coding:utf8

import time
from pylib.WebOp import WebOp
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# 使用css判断元素是否存在的方法
def IsElementPresentcss(element):
    WebOp.shared_wd.implicitly_wait(0.5)
    try:
        WebOp.shared_wd.find_elements_by_css_selector(element)[0]
        WebOp.shared_wd.implicitly_wait(5)
        return True
    except:
        WebOp.shared_wd.implicitly_wait(5)
        return False

# 使用xpath判断元素是否存在的方法
def IsElementPresentxpath(element):
    WebOp.shared_wd.implicitly_wait(0.5)
    try:
        WebOp.shared_wd.find_elements_by_xpath(element)[0]
        WebOp.shared_wd.implicitly_wait(5)
        return True
    except:
        WebOp.shared_wd.implicitly_wait(5)
        return False


# 创建文件目录
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

# 截图的方法(自用)
def ScreenShot(pic_path):
    currentTimeToS = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    currentTimeToD = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    createpath = pic_path + '\\' + currentTimeToD
    mkdir(createpath)
    path = createpath + '\\' + currentTimeToS + '.png'
    WebOp.shared_wd.get_screenshot_as_file(path)

# 从answer.txt中取出答案，txt样式参考answer.txt，每个答案后面带一个空行(answerPath:路径；n：大题数量)
def GetAnswer(answerPath,n):
    with open(answerPath) as answerFile:
        answerList = answerFile.readlines()
        answerListYH = []
        answers = ''
        for titleNo in range(n):
            i = 0
            for answer in answerList:
                answer = answer.decode('utf8')
                if answer == '\n':
                    break
                answers = answers + answer
                i = i + 1
            answerListYH.append(answers)
            answerList = answerList[i+1:]
            answers = ''
    return answerListYH


# 一直等待某元素出现，默认超时10秒
def is_visible(locator, timeout=20):
    try:
        ui.WebDriverWait(WebOp.shared_wd, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# 一直等待某个元素消失，默认超时10秒
def is_not_visible(locator, timeout=20):
    try:
        ui.WebDriverWait(WebOp.shared_wd, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# 对prompt对话框的操作，获取text然后输入并点击确定
def Prompt():
    alertTextele = WebOp.shared_wd.switch_to_alert()
    alertText = alertTextele.text[-2:]
    WebOp.shared_wd.switch_to.alert.send_keys(alertText)
    WebOp.shared_wd.switch_to.alert.accept()


# 切换到对应的handle，参数为title（部分或者全部皆可）
def ChangeHandle(title):
    handles = WebOp.shared_wd.window_handles
    for handle in handles:
        WebOp.shared_wd.switch_to_window(handle)
        WebOp.shared_wd.refresh()
        if title in WebOp.shared_wd.title:
            break

# 获取element的Text，参数为想要获取的text的element的xpath值
def MyGetText(xpath):
    element = WebOp.shared_wd.find_elements_by_xpath(xpath)[0]
    return element.text
# 对某个元素进行点击 使用xpath定位
def MyClickElement(locator):
    try:
        WebOp.shared_wd.find_elements_by_xpath(locator)[0].click()
    except:
        element = WebOp.shared_wd.find_elements_by_xpath(locator)[0]
        element.send_keys(Keys.ENTER)


#  测试

def test():
    # num = GetAnswer('..\\data\\answer\\answer.txt', 7)
    # print type(num[5])
    pass
if __name__ == '__main__':
    test()


