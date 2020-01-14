import unittest
from ddt import ddt,data
from TestData import LoginData
from PageLocators.LoginLocators import LoginLocator
from PageObject.LoginObject import LoginObject

testdatas = LoginData.wrong_login_datas

@ddt
class LoginCase(unittest.TestCase):

    @data(*testdatas)
    def login(self,data):
        print('数据为:%s' % data['user'])
        eles = self.driver.find_elements(LoginLocator.eles)
        print('eles:%s'%eles)
        eles[0].send_keys(data['user'])
        eles[1].send_keys(data['pwd'])
        self.driver.click(LoginLocator.button)
        self.driver.implicitly_wait(10)

        self.assertEqual(data['expect'],data['result'],'实际结果为:%s'%data['result'])

if __name__ == '__main__':
    unittest.main()
