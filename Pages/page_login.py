from selenium.webdriver.common.by import By
from Base.base import BasePage
import time

"""登录"""


class LoginPage(BasePage):


    """元素"""
    url = "https://jinduo.test.kdcloud.com/login.html"
    username = (By.XPATH, '//*[@id="content"]/div/div[3]/div[2]/div[2]/input')
    password = (By.XPATH, '//*[@id="content"]/div/div[3]/div[3]/div[2]/input')
    submit = (By.CLASS_NAME, "EFZRJepJ")
    headtext = (By.XPATH, '//*[@id="homepagetabap"]/div/div[1]/div[1]')
    Continuelogin = (By.CLASS_NAME, "_39-YuAUu")

    """页面操作"""

    def login(self, username, password):
        self.implicitly_wait() #隐式等待全部元素加载
        self.geturl(self.url)
        self.max() #窗口最大化
        self.send_key(loc=self.username, value=username) #定位账号密码位置
        self.send_key(loc=self.password, value=password)
        self.click(loc=self.submit)
        time.sleep(3)
        #如果账号被登陆，强制登录
        try:
            self.loctor(loc=self.Continuelogin)
            self.click(loc=self.Continuelogin)
            time.sleep(3)
        except:
            pass

    # 获取首页断言文本信息
    def shouye_text(self):
        return self.loctor(loc=self.headtext).text


