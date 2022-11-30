from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 显式等待模块
from selenium.webdriver.support.ui import WebDriverWait
# 显式等待条件
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://jinduo.test.kdcloud.com/login.html')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div[2]/div[2]/input').send_keys(
    "13229015420")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div[3]/div[2]/input').send_keys("xxyz2020@")
driver.find_element(By.CLASS_NAME, "EFZRJepJ").click()

# wd是webdriver对象，10是最长等待时间，0.5是每0.5秒去查询对应的元素。until后面跟的等待具体条件，EC是判断条件，检查元素是否存在于页面的 DOM 上。
WebDriverWait(driver, 10, 1.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[1]')))
a = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[1]').text
if "首页" in a:
    print("通过")
else:
    print("不通过")
