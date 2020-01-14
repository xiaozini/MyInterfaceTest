from PageLocators.LoginLocators import LoginLocator
from common.BasePageObject import BasePageObject
from common.readConfig import ReadConfig

baseurl = ReadConfig().get_config('HTTP','baseurl')
print(baseurl)
class LoginObject(BasePageObject):

    def login(self,user,pwd):
        self.driver.get_open(baseurl)
        eles = self.driver.find_elements(LoginLocator.eles)
        eles[0].send_keys(user)
        eles[1].send_keys(pwd)
        self.driver.click(LoginLocator.button)
        self.driver.implicitly_wait(10)
        logout = self.driver.find_element(LoginLocator.logout)
        if logout != "":
            print('登录成功')
        else:
            print('登录失败')

if __name__ == '__main__':
    login = LoginObject()
    login.login('nxk','123')