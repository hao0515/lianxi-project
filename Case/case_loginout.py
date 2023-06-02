from selenium import webdriver
from Pages.page_loginout import LoginoutPage
from Case.case_login import TestLogin
import pytest


class TestLoginout():
    def setup(self):
        TestLogin.test_login(self)

    def test001(self):
        loginout = LoginoutPage(self.driver)
        loginout.loginout()
        loginout_text = loginout.log_text()
        print(loginout_text)
        assert loginout_text == '金舵中台旗舰版(沙箱)账号登录'
