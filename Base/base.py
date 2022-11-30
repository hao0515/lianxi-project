from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    '''
       BasePage封装所有界面都公用的方法。
       例如driver,find_element等
       '''

    # 实例化BasePage类时，事先执行的__init__方法，该方法需要传递参数
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    # 进入网址
    def get(self):
        self.driver.get(self.base_url)

    # 元素定位,替代八大定位
    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    # 点击
    def left_click(self, *locator):
        self.driver.find_element(*locator).click()

    # 输入
    def send_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    #提取文字信息
    def draw_text(self, *locator):
        self.driver.find_element(*locator).text

    # 关闭浏览器
    def quit_driver(self):
        self.driver.quit()

    #等待
    '''
    定位类型字典设计
    手撸框架可以节省很多if...else...代码
    '''
    LOCATION_TYPE = {
        'id': By.ID,
        'name': By.NAME,
        'class': By.CLASS_NAME,
        'tag': By.TAG_NAME,
        'link': By.LINK_TEXT,
        'plink': By.PARTIAL_LINK_TEXT,
        'xpath': By.XPATH,
        'css': By.CSS_SELECTOR
    }

    def waiting_for_element( wait_type, secs=3, type=None, location=None, opr: webdriver.Chrome = None):
        if wait_type == '等待':
            time.sleep(secs)
            return True, '【等待】成功'
        elif wait_type == '隐性等待':
            opr.implicitly_wait(secs)
            return True, '【隐性等待】成功'
        elif wait_type == '显性等待':
            if type is None or location is None or opr is None:
                return False, '【显性等待】请填写所有参数'
            try:
                WebDriverWait(opr, secs, 0.5).until(
                    EC.visibility_of_element_located((LOCATION_TYPE[str.lower(type)], location)))
            except TimeoutException as e:
                return False, '【显性等待】{}秒超时，元素[{}]=[{}]没有出现'.format(str(secs), type, location)
            except Exception as e:
                return False, '【显性等待】传参有误，请检查参数'
