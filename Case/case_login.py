import unittest
from Pages.page_login import LoginPage


class BaiBu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()


    def test001(self):
        self.driver = webdriver.Chrome()
        login = LoginPage(self.driver)
        login.login(username="13229015420", password="xxyz2020@")
        pass



if __name__ == '__main__':
    unittest.main()
