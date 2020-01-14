from telnetlib import EC
from logging import log
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

class BasePageObject(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    #打开浏览器
    def get_open(self,baseUrl):
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            log.error("未找到元素")
            self.get_img()

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            log.error("未找到元素")
            self.get_img()

    def clear_text(self,loc):
        return self.find_element(loc).clear()

    def input_text(self,loc,value):
        self.clear_text(loc)
        self.find_element(loc).send_keys(value)

    def click(self,loc):
        self.find_element(loc).click()
