from common.BasePageObject import BasePageObject
from common.readConfig import ReadConfig
from time import sleep
from selenium.webdriver.common.by import By

url = ReadConfig().get_config('HTTP',"baseurl")
print('url:%s'%url)

class LoginPage(BasePageObject):
    # BasePage().get_open("https://h5-qa.admin.yuedaowang.com/#/login")

    def login(self,user,pwd):
        self.driver.get("https://h5-qa.admin.yuedaowang.com/#/login")
        eles = self.driver.find_elements(By.CSS_SELECTOR,"div input[name='name']")
        eles[0].send_keys(user)
        eles[1].send_keys(pwd)
        button = self.driver.find_element(By.CSS_SELECTOR,'button[type="button"] span')
        button.click()
        sleep(2)
        logout = self.driver.find_element(By.CSS_SELECTOR,'button span')
        if logout != "":
            print('登录成功')
        self.driver.close()

if __name__ == '__main__':
    loginPage = LoginPage()
    loginPage.login('nxk','123')