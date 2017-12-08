# coding:utf8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebOp:

    shared_wd = None

    def openBrowser(self):
        if WebOp.shared_wd:
            return
        options = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=C://Users//wsh/AppData//Local//Google//Chrome//User Data//Default')  # 谷歌浏览器使用我自己的默认设置  设置成我的数据文件
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'c:\\'}
        options.add_experimental_option('prefs', prefs)
        WebOp.shared_wd = webdriver.Chrome(chrome_options=options)
        WebOp.shared_wd.implicitly_wait(5)


    def closeBrowser(self):
        WebOp.shared_wd.quit()



