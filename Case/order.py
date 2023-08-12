from selenium import webdriver
from Pages.page_login import LoginPage
from . import public
import pytest
class TestLoginout:
    #初始化环境
    def setup_class(self):
        self.driver = webdriver.Chrome()
        public.login()

    def test001(self):
        print("调用成功，order")
    def teardown_class(self):
        self.driver.quit() # 关闭浏览器