from selenium.webdriver.common.by import By
from Base.base import BasePage
import time

"""定义元素和操作元素的方法"""


class LoginPage(BasePage):
    """元素"""
    url = "https://jinduo.test.kdcloud.com/login.html"
    username = (By.XPATH, '//*[@id="content"]/div/div[3]/div[2]/div[2]/input')
    password = (By.XPATH, '//*[@id="content"]/div/div[3]/div[3]/div[2]/input')
    submit = (By.CLASS_NAME, "EFZRJepJ")
    text = (By.XPATH, '*[@id="homepagetabap"]/div/div[1]/div[1]')

    """页面操作方法"""

    def login(self, username, password):
        self.geturl(self.url)
        time.sleep(1)
        self.send_key(loc=self.username, value=username)
        time.sleep(1)
        self.send_key(loc=self.password, value=password)
        time.sleep(1)
        self.click(loc=self.submit)
        time.sleep(10)
