from selenium import webdriver
import time

class BasePage(object):
    '''封装每个页面的公用方法'''

    # 浏览器驱动
    def __init__(self, driver):
        self.driver = driver

    """共同方法"""

    # 进入网址
    def geturl(self, url):
        self.driver.get(url)

    # 元素定位方法,替代八大定位
    def loctor(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def send_key(self, loc, value):
        self.loctor(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.loctor(loc).click()

    # # 提取文字信息
    # def text(self, loc):
    #     self.loctor(loc).text

    # 关闭浏览器
    def quit_driver(self):
        self.driver.quit()

