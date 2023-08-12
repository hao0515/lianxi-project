from selenium import webdriver
from Pages.page_login import LoginPage


def login():


    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)  # 保持浏览器执行完不关闭
    login = LoginPage(driver)
    login.login(username="13229015420", password="xxyz2020@")