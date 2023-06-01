import unittest
from selenium import webdriver
from Pages.page_login import LoginPage


class TestLogin(unittest.TestCase):



    def test001(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        login = LoginPage(self.driver)
        login.login(username="13229015420", password="xxyz2020@")
        self.assertEqual('首页',LoginPage.worktable_undo_text(self))