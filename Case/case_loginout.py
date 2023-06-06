from selenium import webdriver
from Pages.page_loginout import LoginoutPage
from Case.case_login import TestLogin
import pytest
"""退出登录"""
class TestLoginout:
    #初始化环境
    def setup_class(self):
        self.driver = webdriver.Chrome()
        TestLogin.test_login(self)

    def test001(self):
        loginout = LoginoutPage(self.driver)
        loginout.loginout()
        loginout_text = loginout.log_text()
        assert '金舵中台旗舰版(沙箱)账号登录' == loginout_text
    def teardown_class(self):
        self.driver.quit() # 关闭浏览器