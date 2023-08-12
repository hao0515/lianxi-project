from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage(object):
    '''封装每个页面的公用方法'''

    # 浏览器驱动
    def __init__(self, driver):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
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

    # 窗口最大化
    def max(self):
        self.driver.maximize_window()
    #隐式等待
    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    #显示等待
    def wait_click(self, loc):
        return WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(loc))
    # 关闭浏览器
    def quit_driver(self):
        self.driver.quit()


