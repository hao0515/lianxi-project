import unittest
from selenium import webdriver
from Pages.page_login import LoginPage


class BaiBu(unittest.TestCase):

    def test001(self):
        self.driver = webdriver.Chrome()
        login = LoginPage(self.driver)
        login.login(username="13229015420", password="xxyz2020@")
