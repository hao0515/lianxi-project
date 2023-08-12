from selenium.webdriver.common.by import By
from Base.base import BasePage
import time

"""订单"""


class LoginPage(BasePage):
    sale_button = (By.CLASS_NAME, "_1PQ5CWW1")
    sale_zx = (By.XPATH, "//*[@id="navigationbar"]/div/div[1]/div[4]/div")
    sale_cl = (By.XPATH, "//*[@id="kd-theme"]/div[7]/ul/li[1]/div/span")
    sale_add = (By.XPATH, "//*[@id="tblnew"]/span/span")
