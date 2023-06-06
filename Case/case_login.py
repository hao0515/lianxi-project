from selenium import webdriver
from Pages.page_login import LoginPage
import pytest

""""登录"""
class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    # 初始化环境
    def test_login(self):

        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('detach', True)
        # self.driver = webdriver.Chrome(chrome_options=options)  # 保持浏览器执行完不关闭
        login = LoginPage(self.driver)
        login.login(username="13229015420", password="xxyz2020@")
        success = login.shouye_text()
        print(success)
        assert '首页' == success

    def teardown_class(self):
        self.driver.quit() # 关闭浏览器