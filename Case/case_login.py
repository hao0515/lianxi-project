from selenium import webdriver
from Pages.page_login import LoginPage


class TestLogin():

    def test_login(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(chrome_options=options)  # 保持浏览器执行完不关闭

        # self.driver = webdriver.Chrome()
        login = LoginPage(self.driver)
        login.login(username="13229015420", password="xxyz2020@")
        success = login.shouye_text()
        print(success)
        assert '首页' == success
