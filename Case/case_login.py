import unittest
from selenium import webdriver
from Pages.page_login import SearchOne
import time


class BaiBu(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()


    def test001(self):

        url = "https://jinduo.test.kdcloud.com/login.html"
        s = SearchOne(self.driver, url)
        s.open_baidu()
        time.sleep(2)
        s.input_username("13229015420")
        s.input_password("xxyz2020@")
        s.click_baidu_search()
        s.loading()
        equal = self.location(self)
        self.assertIn("首页", equal)

    def tearDown(self) -> None:
        #      self.driver.quit()
        pass



if __name__ == '__main__':
    unittest.main()
