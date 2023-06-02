from selenium.webdriver.common.by import By
from Base.base import BasePage
import time

"""定义元素和操作元素的方法"""


class LoginoutPage(BasePage):


    """元素"""
    head_picture = (By.XPATH, '//*[@id="usericon"]')
    login_out = (By.XPATH, '//*[@id="flexpanelap12"]/a[3]/span')
    login_text = (By.ID, "kd_cloud_title")

    """页面操作方法"""

    def loginout(self):
        try:

            self.wait_click(loc=self.head_picture)
            self.click(loc=self.head_picture)
            #time.sleep(4)
            self.wait_click(loc=self.login_out)
            self.click(loc=self.login_out)
        except :

            time.sleep(3)
            self.click(loc=self.head_picture)
            # time.sleep(4)
            self.click(loc=self.login_out)



    # 获取首页断言文本信息
    def log_text(self):
        return self.loctor(loc=self.login_text).text