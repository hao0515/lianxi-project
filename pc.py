import time

from selenium import webdriver
# 导入元素定位类型枚举
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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


def waiting_for_element(wait_type, secs=3, type=None, location=None, opr: webdriver.Chrome = None):
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
