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
    headtext = (By.XPATH, '//*[@id="homepagetabap"]/div/div[1]/div[1]')
    Continuelogin = (By.CLASS_NAME, "_39-YuAUu")

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

    # 首页断言 （定位分离）
    def worktable_undo(self):
        return self.loctor(loc=self.headtext)

    # 获取首页断言文本信息 （操作元素动作分离）
    def worktable_undo_text(self):
        return self.worktable_undo().text


