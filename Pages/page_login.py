from selenium.webdriver.common.by import By

from Base.base import BasePage

from selenium import webdriver

class SearchOne(BasePage):
    def __init__(self, driver, url):
        BasePage.__init__(self, driver, url)

    # 进入登录页面
    def open_baidu(self):
        self.get()

    # 输入数据
    def input_username(self, text):
        self.send_text(text, By.XPATH, '//*[@id="content"]/div/div[3]/div[2]/div[2]/input')

    def input_password(self, text):
        self.send_text(text, By.XPATH, '//*[@id="content"]/div/div[3]/div[3]/div[2]/input')

    # 点击按钮
    def click_baidu_search(self):
        self.left_click(By.CLASS_NAME, "EFZRJepJ")

    # 选择文字“首页”为判断条件
    def location(self):
        self.draw_text(By.XPATH, '*[@id="homepagetabap"]/div/div[1]/div[1]')
        return self.location(self)




