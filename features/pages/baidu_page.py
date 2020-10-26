

'''
定义百度首页的page类，提供给steps使用

'''
import time


class baidu_page():

    def __init__(self,driver):
        print('初始化baidu_page类')
        self.driver = driver

    def GetUrl(self,url):
        self.driver.get(url)

    def InputAndSearch(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def ClosePage(self):
        self.driver.close()



